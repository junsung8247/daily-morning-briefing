@echo off
chcp 65001 > nul
cd /d "C:\데일리 모닝 브리핑"
python "C:\데일리 모닝 브리핑\scripts\check_and_catchup.py"
