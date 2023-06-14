echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 20731 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10964) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15792) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 336) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17624) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15524) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19076)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_09-13\cleanup-fluent-wenzheshang-15524.bat"
