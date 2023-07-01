echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 30235 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18412) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22156) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10396) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19544) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 13888) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15644)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-07-01_17-15\cleanup-fluent-wenzheshang-13888.bat"
