echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1316 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18764) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10440) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18180) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18804) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 6176) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16644)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-20_17-20\cleanup-fluent-wenzheshang-6176.bat"
