echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 29298 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12284) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 5848) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 4856) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10840) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 5484) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14756)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_09-32\cleanup-fluent-wenzheshang-5484.bat"
