echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 1114 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18876) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 4784) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22516)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-29_21-38\cleanup-fluent-wenzheshang-4784.bat"
