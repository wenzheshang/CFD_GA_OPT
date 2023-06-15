echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1212 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10348) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15872) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16196) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22184) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17240) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23488)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-15_21-33\cleanup-fluent-wenzheshang-17240.bat"
