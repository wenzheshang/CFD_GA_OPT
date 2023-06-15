echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1200 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14684) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18572) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20364) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10676) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23664) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9556)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-15_16-23\cleanup-fluent-wenzheshang-23664.bat"
