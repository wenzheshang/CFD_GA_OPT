echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 23045 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17360) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20360) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 13692)
del "f:\Thinking\program\pareto_front\lib\Workdata\Fluent_Python\2023-05-28_20-36\cleanup-fluent-wenzheshang-20360.bat"
