echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 31073 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9380) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 4484) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17428) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14624) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 2136) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19132)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_18-20\cleanup-fluent-wenzheshang-2136.bat"
