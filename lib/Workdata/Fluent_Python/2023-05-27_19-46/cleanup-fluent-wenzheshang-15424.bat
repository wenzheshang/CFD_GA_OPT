echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 52211 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10764) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15424) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15836)
del "f:\Thinking\program\pareto_front\lib\Workdata\Fluent_Python\2023-05-27_19-46\cleanup-fluent-wenzheshang-15424.bat"
