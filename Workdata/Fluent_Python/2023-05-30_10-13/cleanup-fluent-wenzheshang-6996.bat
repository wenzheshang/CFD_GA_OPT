echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1253 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 9928) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17888) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18872) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 8368) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 6996) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10540)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_10-13\cleanup-fluent-wenzheshang-6996.bat"
