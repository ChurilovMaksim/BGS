#!/bin/bash
cd "C:/Users/churi/Desktop/BGS/BGS/BGS"
L=review/audit_2026-08-29/logs
for s in catmap_independent verify_mean_law theoremB_covariance theta_square_theorem parity_desymmetrised theoremE_operator lemmaF_quadratic_phase moment_certification subgroup_kloosterman_energy barrier_slack pstar_scan; do
  echo "=== $s ===" >> $L/core_certs.log
  t0=$SECONDS
  python src/$s.py > $L/$s.out 2> $L/$s.err
  ec=$?
  echo "exit=$ec elapsed=$((SECONDS-t0))s" >> $L/core_certs.log
done
echo ALL_DONE >> $L/core_certs.log
