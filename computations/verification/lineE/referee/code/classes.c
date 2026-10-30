/* Independent class-sum engine (auditor's code).
   Enumerate all period-m q-sequences z_j in Z/h with z_{j+1} = 6 z_j - z_{j-1} (mod h), (z0,z1) in (Z/h)^2,
   Phi(z) = prod_{j<m} tab[z_j]   (tab[k] = g(1/2 + k/h)),
   T[r] += Phi(z) for r = Q(z) = z0^2 - 6 z0 z1 + z1^2 mod h.
   usage: classes m h tab.bin out.bin   (complex double arrays) */
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <omp.h>
int main(int argc,char**argv){
  int m=atoi(argv[1]); long h=atol(argv[2]);
  double complex *tab=malloc(sizeof(double complex)*h);
  FILE*f=fopen(argv[3],"rb"); if(fread(tab,sizeof(double complex),h,f)!=(size_t)h){fprintf(stderr,"bad tab\n");return 1;} fclose(f);
  int nt=omp_get_max_threads();
  long double complex *T=calloc((size_t)nt*h,sizeof(long double complex));
  #pragma omp parallel for schedule(dynamic,16)
  for(long z0=0;z0<h;z0++){
    int t=omp_get_thread_num(); long double complex *Tt=T+(size_t)t*h;
    for(long z1=0;z1<h;z1++){
      long a=z0,b=z1; double complex p=tab[a]*tab[b];
      for(int j=2;j<m;j++){ long c=(6*b-a)%h; if(c<0)c+=h; a=b;b=c; p*=tab[b]; }
      long r=( (z0*z0)%h - (6*z0%h)*z1%h + (z1*z1)%h )%h; if(r<0)r+=h; r%=h;
      Tt[r]+=p;
    }
  }
  double complex *out=malloc(sizeof(double complex)*h);
  for(long r=0;r<h;r++){ long double complex s=0; for(int t=0;t<nt;t++) s+=T[(size_t)t*h+r]; out[r]=(double complex)s; }
  f=fopen(argv[4],"wb"); fwrite(out,sizeof(double complex),h,f); fclose(f);
  return 0;
}
