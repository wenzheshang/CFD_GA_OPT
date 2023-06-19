echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 5162 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 8976) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 4740) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 16820) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 15340) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 17748) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 18716)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-19_22-20\cleanup-fluent-wenzheshang-17748.bat"
