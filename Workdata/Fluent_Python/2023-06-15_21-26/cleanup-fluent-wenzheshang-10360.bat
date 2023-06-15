echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1849 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20640) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21360) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 25032) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22704) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10360) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23976)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-15_21-26\cleanup-fluent-wenzheshang-10360.bat"
