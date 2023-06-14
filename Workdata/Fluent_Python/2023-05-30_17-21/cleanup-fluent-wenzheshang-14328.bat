echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1622 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21680) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 26452) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23120) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23416) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14328) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21804)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_17-21\cleanup-fluent-wenzheshang-14328.bat"
