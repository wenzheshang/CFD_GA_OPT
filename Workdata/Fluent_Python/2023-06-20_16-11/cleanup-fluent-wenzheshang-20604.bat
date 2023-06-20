echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1376 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16448) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21420) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10884) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22044) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20604) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21624)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-20_16-11\cleanup-fluent-wenzheshang-20604.bat"
