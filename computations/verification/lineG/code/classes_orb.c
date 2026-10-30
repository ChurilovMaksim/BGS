/* Line G orbit-canonical class-sum engine (independent of audit classes.c).
   T[r] = sum_{z in (Z/h)^2} Phi(z),  Phi(z)=prod_{j<m} tab[z_j], z_{j+1}=6z_j-z_{j-1} mod h, r=Q(z)=z0^2-6z0z1+z1^2 mod h.
   Phi and Q are invariant under the shift (z0,z1)->(z1,z2). We visit each shift-orbit once, at its lexicographically
   minimal pair (z_j,z_{j+1}), and add (orbit size)*Phi.  Requires S^m = I mod h (true: lambda^m = 1 mod h for odd m).
   usage: classes_orb m h tab.bin out.bin */
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <omp.h>
static inline long step(long a,long b,long h){ long x=6*b-a; if(x<0) x+=h; while(x>=h) x-=h; return x; }
int main(int argc,char**argv){
  int m=atoi(argv[1]); long h=atol(argv[2]);
  double complex *tab=malloc(sizeof(double complex)*h);
  FILE*f=fopen(argv[3],"rb"); if(fread(tab,sizeof(double complex),h,f)!=(size_t)h){fprintf(stderr,"bad tab\n");return 1;} fclose(f);
  int nt=omp_get_max_threads();
  long double complex *T=calloc((size_t)nt*h,sizeof(long double complex));
  long ncanon=0, nbad=0; long done=0;
  #pragma omp parallel for schedule(dynamic,1) reduction(+:ncanon,nbad)
  for(long z0=0;z0<h;z0++){
    int t=omp_get_thread_num(); long double complex *Tt=T+(size_t)t*h;
    long zz[130];
    for(long z1=z0;z1<h;z1++){
      /* quick reject: z_{-1} = 6 z0 - z1 must be >= z0 (or equal with tie handled in full check) */
      long zm1 = step(z1,z0,h); /* 6*z0 - z1 */
      if(zm1<z0) continue;
      long a=z0,b=z1; int ok=1; int j;
      zz[0]=z0; zz[1]=z1;
      for(j=2;j<=m;j++){ long c=step(a,b,h); if(c<z0){ok=0;break;} zz[j]=c; a=b;b=c; }
      if(!ok) continue;
      /* now z_0..z_m all >= z0, and z_m must equal z0, z_{m+1}=z1 (period divides m) */
      long zmp1=step(zz[m-1],zz[m],h);
      if(zz[m]!=z0 || zmp1!=z1){ nbad++; continue; }
      /* lexicographic minimality and stabilizer count */
      int stab=1; int minimal=1;
      for(j=1;j<m;j++){ long u=zz[j], v=zz[j+1];
        if(u==z0){ if(v<z1){minimal=0;break;} if(v==z1) stab++; } }
      if(!minimal) continue;
      int per = m/stab;  /* orbit size */
      double complex p=1; for(j=0;j<m;j++) p*=tab[zz[j]];
      long r=((z0*z0)%h - (6*z0%h)*z1%h + (z1*z1)%h)%h; if(r<0)r+=h;
      Tt[r]+=(long double complex)(per*p); ncanon++;
    }
    #pragma omp atomic
    done++;
    if((done%20000)==0){ fprintf(stderr,"progress %ld/%ld\n",done,h); fflush(stderr);}
  }
  double complex *out=malloc(sizeof(double complex)*h);
  for(long r=0;r<h;r++){ long double complex s=0; for(int t=0;t<nt;t++) s+=T[(size_t)t*h+r]; out[r]=(double complex)s; }
  f=fopen(argv[4],"wb"); fwrite(out,sizeof(double complex),h,f); fclose(f);
  fprintf(stderr,"canonical orbits %ld, period-check failures %ld\n",ncanon,nbad);
  return 0;
}
