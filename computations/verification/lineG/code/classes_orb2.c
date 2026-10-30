/* Line G class sums, canonical representatives under the group <shift, z->-z> (order 2m) -- valid when
   tab[k]==tab[(h-k)%h] (checked).  Visit (z0,z1) only if it is lexicographically minimal among all
   (z_j,z_{j+1}) and (-z_j,-z_{j+1}) mod h, j=0..m-1; add (orbit size)*Phi.  usage: classes_orb2 m h tab.bin out.bin */
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <omp.h>
static inline long step(long a,long b,long h){ long x=6*b-a; if(x<0) x+=h; while(x>=h) x-=h; return x; }
int main(int argc,char**argv){
  int m=atoi(argv[1]); long h=atol(argv[2]);
  double complex *tab=malloc(sizeof(double complex)*h);
  FILE*f=fopen(argv[3],"rb"); if(fread(tab,sizeof(double complex),h,f)!=(size_t)h){fprintf(stderr,"bad tab\n");return 1;} fclose(f);
  for(long k=1;k<h;k++) if(cabs(tab[k]-tab[h-k])>1e-13){fprintf(stderr,"tab not symmetric\n");return 4;}
  int nt=omp_get_max_threads();
  long double complex *T=calloc((size_t)nt*h,sizeof(long double complex));
  long ncanon=0, nbad=0, done=0; long half=h/2;
  #pragma omp parallel for schedule(dynamic,1) reduction(+:ncanon,nbad)
  for(long z0=0;z0<=half;z0++){
    int t=omp_get_thread_num(); long double complex *Tt=T+(size_t)t*h;
    long zz[130]; long lo=z0, hi=(z0==0)?h-1:h-z0;   /* all z_j must lie in [z0, h-z0] (or be 0 when z0==0) */
    for(long z1=z0;z1<h;z1++){
      if(z0>0 && z1>hi) break;
      long zm1=step(z1,z0,h);
      if(z0>0 && (zm1<lo||zm1>hi)) continue;
      if(z0==0 && zm1!=0 && 0) continue;
      long a=z0,b=z1; int ok=1,j; zz[0]=z0; zz[1]=z1;
      for(j=2;j<=m;j++){ long c=step(a,b,h); if(z0>0 && (c<lo||c>hi)){ok=0;break;} zz[j]=c; a=b;b=c; }
      if(!ok) continue;
      long zmp1=step(zz[m-1],zz[m],h);
      if(zz[m]!=z0||zmp1!=z1){nbad++;continue;}
      int stab=0, minimal=1;
      for(j=0;j<m && minimal;j++){
        long u=zz[j], v=zz[j+1];
        if(u==z0){ if(v<z1){minimal=0;break;} if(v==z1) stab++; }
        long un=(h-u)%h, vn=(h-v)%h;
        if(un==z0){ if(vn<z1){minimal=0;break;} if(vn==z1) stab++; }
        if(u<z0 || un<z0){minimal=0;break;}
      }
      if(!minimal) continue;
      int per=(2*m)/stab;
      double complex p=1; for(j=0;j<m;j++) p*=tab[zz[j]];
      long r=((z0*z0)%h - (6*z0%h)*z1%h + (z1*z1)%h)%h; if(r<0)r+=h;
      Tt[r]+=(long double complex)(per*p); ncanon++;
    }
    #pragma omp atomic
    done++;
    if((done%50000)==0){ fprintf(stderr,"progress %ld/%ld\n",done,half+1); fflush(stderr);}
  }
  double complex *out=malloc(sizeof(double complex)*h);
  for(long r=0;r<h;r++){ long double complex s=0; for(int t=0;t<nt;t++) s+=T[(size_t)t*h+r]; out[r]=(double complex)s; }
  f=fopen(argv[4],"wb"); fwrite(out,sizeof(double complex),h,f); fclose(f);
  fprintf(stderr,"canonical %ld bad %ld\n",ncanon,nbad); return 0;
}
