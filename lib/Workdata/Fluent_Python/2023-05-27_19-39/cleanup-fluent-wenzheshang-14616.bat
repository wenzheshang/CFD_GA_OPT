echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 51725 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 7988) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14616) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16568)
del "f:\Thinking\program\pareto_front\lib\Workdata\Fluent_Python\2023-05-27_19-39\cleanup-fluent-wenzheshang-14616.bat"
