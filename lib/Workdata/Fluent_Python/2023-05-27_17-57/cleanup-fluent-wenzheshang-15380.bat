echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 19677 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21832) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15380) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 24492)
del "f:\Thinking\program\pareto_front\lib\Workdata\Fluent_Python\2023-05-27_17-57\cleanup-fluent-wenzheshang-15380.bat"
