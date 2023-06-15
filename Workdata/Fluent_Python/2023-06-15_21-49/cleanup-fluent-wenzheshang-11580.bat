echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 22609 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 23220) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14784) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 24052) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 11076) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 11580) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 20256)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-15_21-49\cleanup-fluent-wenzheshang-11580.bat"
