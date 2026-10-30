/* Rigorous-rounding kernel for S_t = sum_{(z0,z1) in (Z/h)^2} E[(t*R(z)) mod h] * prod_{j<m} G[z_j],
   z_j = (a_j z0 + b_j z1) mod h, R(z) = A z0^2 + B z0 z1 + C z1^2 mod h, for a list of t.
   E[k] = e(k/h), G[k] = g(1/2 + k/h) given as double tables (rounded from arb by the driver).
   Plain IEEE double arithmetic, explicit real formulas, compiled with -ffp-contract=off (no FMA contraction), no fast-math.
   Row sums in double, row totals accumulated in long double.  Error bound computed by the driver (a priori).
   usage: zres m h tabfile coeffile nt t1 t2 ... outfile */
/* The a-priori error bound assumes no FMA contraction (see resonant_residue_lineE.md, section 10.3, and build_zres.sh). */
#pragma GCC optimize("fp-contract=off")
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>
int main(int argc,char**argv){
  int m=atoi(argv[1]); int64_t h=atoll(argv[2]); const char*tf=argv[3]; const char*cf=argv[4]; int nt=atoi(argv[5]);
  int64_t t[8]; for(int i=0;i<nt;i++) t[i]=atoll(argv[6+i]); const char*of=argv[6+nt];
  double *G=malloc(sizeof(double)*2*h), *E=malloc(sizeof(double)*2*h);
  FILE*f=fopen(tf,"rb"); if(fread(G,sizeof(double),2*h,f)!=(size_t)(2*h)||fread(E,sizeof(double),2*h,f)!=(size_t)(2*h)){fprintf(stderr,"bad tab\n");return 1;} fclose(f);
  int64_t a[64],b[64],A,B,C; f=fopen(cf,"r");
  for(int j=0;j<m;j++) if(fscanf(f,"%ld %ld",&a[j],&b[j])!=2) return 2;
  if(fscanf(f,"%ld %ld %ld",&A,&B,&C)!=3) return 3; fclose(f);
  long double SR[8]={0},SI[8]={0};
  #pragma omp parallel
  {
    long double sr[8]={0},si[8]={0};
    int64_t z[64];
    #pragma omp for schedule(dynamic,4)
    for(int64_t z0=0;z0<h;z0++){
      for(int j=0;j<m;j++) z[j]=(a[j]*z0)%h;          /* z1 = 0 */
      int64_t U[8],D[8];                              /* U = t*R(z0,z1) mod h ; D = t*(B z0 + C(2 z1 + 1)) mod h */
      int64_t R0=(A%h)*(z0%h)%h*z0%h;  /* A z0^2 */
      int64_t twoC=(2*C)%h;
      for(int i=0;i<nt;i++){ U[i]=(t[i]%h)*R0%h; D[i]=(t[i]%h)*(((B*z0)%h + C)%h)%h; }
      int64_t dt2[8]; for(int i=0;i<nt;i++) dt2[i]=(t[i]%h)*twoC%h;
      double rr[8]={0},ri[8]={0};
      for(int64_t z1=0;z1<h;z1++){
        double pr=G[2*z[0]], pi=G[2*z[0]+1];
        for(int j=1;j<m;j++){ double gr=G[2*z[j]], gi=G[2*z[j]+1]; double nr=pr*gr-pi*gi; double ni=pr*gi+pi*gr; pr=nr; pi=ni; }
        for(int i=0;i<nt;i++){ double er=E[2*U[i]], ei=E[2*U[i]+1]; rr[i]+=pr*er-pi*ei; ri[i]+=pr*ei+pi*er;
          U[i]+=D[i]; if(U[i]>=h) U[i]-=h; D[i]+=dt2[i]; if(D[i]>=h) D[i]-=h; }
        for(int j=0;j<m;j++){ z[j]+=b[j]; if(z[j]>=h) z[j]-=h; }
      }
      for(int i=0;i<nt;i++){ sr[i]+=rr[i]; si[i]+=ri[i]; }
    }
    #pragma omp critical
    for(int i=0;i<nt;i++){ SR[i]+=sr[i]; SI[i]+=si[i]; }
  }
  f=fopen(of,"w"); for(int i=0;i<nt;i++) fprintf(f,"%ld %.17Le %.17Le\n",t[i],SR[i],SI[i]); fclose(f);
  return 0;
}
