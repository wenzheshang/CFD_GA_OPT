echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 23037 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9352) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18956) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 8400) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21568) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12036) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16760)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_08-59\cleanup-fluent-wenzheshang-12036.bat"
