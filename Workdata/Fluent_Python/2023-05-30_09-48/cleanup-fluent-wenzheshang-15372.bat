echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 29968 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10648) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 7172) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18140) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16364) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15372) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12684)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_09-48\cleanup-fluent-wenzheshang-15372.bat"
