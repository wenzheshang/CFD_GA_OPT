echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 23168 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22412) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22188) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19788) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12636) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9624) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16800)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-15_22-06\cleanup-fluent-wenzheshang-9624.bat"
