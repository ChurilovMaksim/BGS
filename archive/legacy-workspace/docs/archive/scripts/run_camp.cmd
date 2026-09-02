@echo off
cd /d C:\Users\churi\Desktop\BGS
py -3 src\campaign.py 1 > artifacts\camp_log1.txt 2>&1
py -3 src\campaign.py 2 > artifacts\camp_log2.txt 2>&1
py -3 src\campaign.py 3 > artifacts\camp_log3.txt 2>&1
py -3 src\campaign.py 4 > artifacts\camp_log4.txt 2>&1
echo DONE > artifacts\camp_done.txt
