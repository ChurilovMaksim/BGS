/* Auditor's independent rigorous kernel: directed-rounding (FE_UPWARD) interval arithmetic.
   Interval x = [lo,hi] stored as (n = -lo, p = hi).  All ops in round-upward mode => outward enclosures.
   S(t) = sum_{z0,z1 in Z/h} E[t*R(z) mod h] * prod_{j<m} G[(a_j z0 + b_j z1) mod h]
   usage: ivsum m h tabfile coeffile nt t1..tnt outfile    (tabfile: G then E, each h entries of 4 doubles: re_n re_p im_n im_p) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <fenv.h>
#include <omp.h>
#pragma STDC FENV_ACCESS ON
typedef struct { double n, p; } iv;              /* [-n, p] */
typedef struct { iv r, i; } civ;
static inline double mx(double a, double b){ return a > b ? a : b; }
static inline iv iadd(iv a, iv b){ iv c = { a.n + b.n, a.p + b.p }; return c; }
static inline iv ineg(iv a){ iv c = { a.p, a.n }; return c; }
static inline iv imul(iv a, iv b){
  double al = -a.n, ah = a.p, bl = -b.n, bh = b.p;   /* exact negations */
  iv c;
  c.p = mx(mx(al*bl, al*bh), mx(ah*bl, ah*bh));          /* each rounded up */
  c.n = mx(mx((-al)*bl, (-al)*bh), mx((-ah)*bl, (-ah)*bh)); /* rounded-up -(x*y) */
  return c;
}
static inline civ cmul(civ x, civ y){
  civ z; z.r = iadd(imul(x.r, y.r), ineg(imul(x.i, y.i))); z.i = iadd(imul(x.r, y.i), imul(x.i, y.r)); return z;
}
int main(int argc, char **argv){
  int m = atoi(argv[1]); int64_t h = atoll(argv[2]); int nt = atoi(argv[5]); int64_t t[8]; for (int i = 0; i < nt; i++) t[i] = atoll(argv[6+i]) % h; const char *outf = argv[6+nt];
  civ *G = malloc(sizeof(civ)*h), *E = malloc(sizeof(civ)*h);
  FILE *f = fopen(argv[3], "rb");
  for (int64_t k = 0; k < h; k++){ double v[4]; if (fread(v, 8, 4, f) != 4) return 1; G[k].r.n=v[0]; G[k].r.p=v[1]; G[k].i.n=v[2]; G[k].i.p=v[3]; }
  for (int64_t k = 0; k < h; k++){ double v[4]; if (fread(v, 8, 4, f) != 4) return 1; E[k].r.n=v[0]; E[k].r.p=v[1]; E[k].i.n=v[2]; E[k].i.p=v[3]; }
  fclose(f);
  int64_t a[64], b[64], A, B, C; f = fopen(argv[4], "r");
  for (int j = 0; j < m; j++) if (fscanf(f, "%ld %ld", &a[j], &b[j]) != 2) return 2;
  if (fscanf(f, "%ld %ld %ld", &A, &B, &C) != 3) return 3; fclose(f);
  civ tot[8]; for (int i=0;i<8;i++){ tot[i].r.n=tot[i].r.p=tot[i].i.n=tot[i].i.p=0; } int badmode = 0;
  #pragma omp parallel
  {
    if (fesetround(FE_UPWARD) != 0 || fegetround() != FE_UPWARD) { 
      #pragma omp atomic
      badmode++; }
    volatile double one = 1.0, tiny = 1e-30;   /* runtime self-test of the rounding mode */
    if (one + tiny == 1.0 || -(-one - tiny) != 1.0) {
      #pragma omp atomic
      badmode++; }
    civ loc[8]; for (int i=0;i<8;i++){ loc[i].r.n=loc[i].r.p=loc[i].i.n=loc[i].i.p=0; }
    #pragma omp for schedule(dynamic, 8)
    for (int64_t z0 = 0; z0 < h; z0++){
      int64_t az[64]; for (int j = 0; j < m; j++) az[j] = (a[j] * z0) % h;
      int64_t Az2 = (A * z0) % h * z0 % h, Bz0 = (B * z0) % h;
      civ row[8]; for (int i=0;i<8;i++){ row[i].r.n=row[i].r.p=row[i].i.n=row[i].i.p=0; }
      for (int64_t z1 = 0; z1 < h; z1++){
        civ p = G[(az[0] + b[0] * z1) % h];
        for (int j = 1; j < m; j++) p = cmul(p, G[(az[j] + (b[j] * z1) % h) % h]);
        int64_t R = (Az2 + Bz0 * z1 % h + (C * z1) % h * z1 % h) % h;
        for (int i = 0; i < nt; i++){ civ q = cmul(p, E[t[i] * R % h]);
          row[i].r = iadd(row[i].r, q.r); row[i].i = iadd(row[i].i, q.i); }
      }
      for (int i = 0; i < nt; i++){ loc[i].r = iadd(loc[i].r, row[i].r); loc[i].i = iadd(loc[i].i, row[i].i); }
    }
    #pragma omp critical
    { for (int i = 0; i < nt; i++){ tot[i].r = iadd(tot[i].r, loc[i].r); tot[i].i = iadd(tot[i].i, loc[i].i); } }
  }
  if (badmode) { fprintf(stderr, "rounding mode not set\n"); return 9; }
  f = fopen(outf, "w");
  for (int i = 0; i < nt; i++) fprintf(f, "%ld %.17e %.17e %.17e %.17e\n", t[i], -tot[i].r.n, tot[i].r.p, -tot[i].i.n, tot[i].i.p);  /* -n is exact */
  fclose(f); return 0;
}
