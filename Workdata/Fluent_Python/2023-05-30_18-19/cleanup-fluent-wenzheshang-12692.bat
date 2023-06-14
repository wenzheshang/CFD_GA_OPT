echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 30934 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16324) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19032) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17064) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18864) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12692) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 19332)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_18-19\cleanup-fluent-wenzheshang-12692.bat"
