echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 19573 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 26296) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22704) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20336)
del "f:\Thinking\program\pareto_front\lib\Workdata\Fluent_Python\2023-05-27_17-56\cleanup-fluent-wenzheshang-22704.bat"
