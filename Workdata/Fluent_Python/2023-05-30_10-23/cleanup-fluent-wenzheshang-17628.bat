echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1542 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 1532) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23528) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 6416) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 3012) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17628) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 3212)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_10-23\cleanup-fluent-wenzheshang-17628.bat"
