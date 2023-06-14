echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 2626 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19804) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19680) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16064) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21324) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14424) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18572)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_22-23\cleanup-fluent-wenzheshang-14424.bat"
