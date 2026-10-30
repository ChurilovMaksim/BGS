/* Line G class-sum engine using the z -> -z symmetry (valid when tab[k]=tab[h-k], i.e. g(1/2+x)=g(1/2-x)).
   T[r] = sum over (z0,z1) in (Z/h)^2 of prod_{j<m} tab[z_j], z_{j+1}=6z_j-z_{j-1}, r = z0^2-6z0z1+z1^2 mod h.
   Pairs {z,-z} counted once with weight 2; (0,0) once.  usage: classes_sym m h tab.bin out.bin  */
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <omp.h>
int main(int argc,char**argv){
  int m=atoi(argv[1]); long h=atol(argv[2]);
  double complex *tab=malloc(sizeof(double complex)*h);
  FILE*f=fopen(argv[3],"rb"); if(fread(tab,sizeof(double complex),h,f)!=(size_t)h){fprintf(stderr,"bad tab\n");return 1;} fclose(f);
  for(long k=1;k<h;k++) if(cabs(tab[k]-tab[h-k])>1e-12){fprintf(stderr,"tab not symmetric at %ld\n",k);return 4;}
  int nt=omp_get_max_threads();
  long double complex *T=calloc((size_t)nt*h,sizeof(long double complex));
  long half=(h-1)/2; long done=0;
  #pragma omp parallel for schedule(dynamic,8)
  for(long z0=0;z0<=half;z0++){
    int t=omp_get_thread_num(); long double complex *Tt=T+(size_t)t*h;
    long z1lo = (z0==0)?1:0;
    double complex acc_dummy=0;
    for(long z1=z1lo;z1<h;z1++){
      if(z0==0 && z1>half) break;
      long a=z0,b=z1; double complex p=tab[a]*tab[b];
      for(int j=2;j<m;j++){ long c=(6*b-a)%h; if(c<0)c+=h; a=b;b=c; p*=tab[b]; }
      long r=((z0*z0)%h - (6*z0%h)*z1%h + (z1*z1)%h)%h; if(r<0)r+=h;
      Tt[r]+=2*p;
    }
    (void)acc_dummy;
    #pragma omp atomic
    done++;
    if(t==0 && (done%2000)==0){ fprintf(stderr,"progress %ld/%ld\n",done,half+1); fflush(stderr);}
  }
  { double complex p=1; for(int j=0;j<m;j++) p*=tab[0]; T[0]+=p; }
  double complex *out=malloc(sizeof(double complex)*h);
  for(long r=0;r<h;r++){ long double complex s=0; for(int t=0;t<nt;t++) s+=T[(size_t)t*h+r]; out[r]=(double complex)s; }
  f=fopen(argv[4],"wb"); fwrite(out,sizeof(double complex),h,f); fclose(f);
  return 0;
}
