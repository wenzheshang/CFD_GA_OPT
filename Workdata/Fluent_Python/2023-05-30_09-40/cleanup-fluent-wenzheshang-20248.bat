echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 29568 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 11932) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9324) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10916) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 5480) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20248) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18764)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_09-40\cleanup-fluent-wenzheshang-20248.bat"
