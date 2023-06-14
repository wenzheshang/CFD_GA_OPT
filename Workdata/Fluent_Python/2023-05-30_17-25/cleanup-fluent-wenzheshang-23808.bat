echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1824 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 26360) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22808) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 25204) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 25356) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23808) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20912)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_17-25\cleanup-fluent-wenzheshang-23808.bat"
