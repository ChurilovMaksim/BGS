#!/bin/bash
# N20: stop the sequential run after shell 13 (shell 14 is done by 3 shards)
cd /workspace/bgs-lineN/N20/logs
while ! grep -q '^13 ' a_cert_ext.out; do sleep 10; done
pkill -f 'a_cert_ext.py 13 14'
