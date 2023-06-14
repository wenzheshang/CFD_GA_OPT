echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 23205 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 10276) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 22216) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12484) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12720) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 8132) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 11904)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-05-30_09-01\cleanup-fluent-wenzheshang-8132.bat"
