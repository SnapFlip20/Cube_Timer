@echo off
title git_push_program
mode con cols=100 lines=30
:main
git add .
git commit -m "CubeTimer_v0.3.0"
git push
echo done
pause>nul
