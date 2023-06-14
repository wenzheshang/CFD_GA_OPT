echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 3100 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23320) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22636) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 3772) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23528) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9380) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22384)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_22-34\cleanup-fluent-wenzheshang-9380.bat"
