echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 50905 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 1176) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9940) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15704)
del "f:\Thinking\program\pareto_front\lib\Workdata\Fluent_Python\2023-05-27_19-26\cleanup-fluent-wenzheshang-9940.bat"
