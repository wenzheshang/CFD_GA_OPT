echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1286 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14808) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 21900) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14956)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_21-43\cleanup-fluent-wenzheshang-21900.bat"
