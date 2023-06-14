echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 30219 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12708) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16560) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9748)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_21-36\cleanup-fluent-wenzheshang-16560.bat"
