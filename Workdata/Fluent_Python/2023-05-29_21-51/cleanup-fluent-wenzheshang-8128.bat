echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1780 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 7400) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 8128) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16508)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_21-51\cleanup-fluent-wenzheshang-8128.bat"
