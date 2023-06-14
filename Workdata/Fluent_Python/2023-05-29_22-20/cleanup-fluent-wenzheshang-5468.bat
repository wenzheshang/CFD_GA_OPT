echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 2399 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 636) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 6904) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 11692) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23268) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 5468) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10892)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_22-20\cleanup-fluent-wenzheshang-5468.bat"
