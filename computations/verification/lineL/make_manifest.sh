#!/bin/bash
cd /workspace/bgs-lineL
find . -type f ! -name 'SHA256_L.txt' ! -name 'SHA256_L.txt.sha256' ! -name '*.err' ! -path './L2/*' | sort | xargs sha256sum > SHA256_L.txt
sha256sum SHA256_L.txt > SHA256_L.txt.sha256
sha256sum -c SHA256_L.txt --quiet && echo manifest OK
