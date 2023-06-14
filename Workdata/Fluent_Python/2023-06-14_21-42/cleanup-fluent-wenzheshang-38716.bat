echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="F:\ANASYS\ANSYS Inc\v202\fluent/ntbin/win64/winkill.exe"

"F:\ANASYS\ANSYS Inc\v202\fluent\ntbin\win64\tell.exe" wenzheshang 21150 CLEANUP_EXITING
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 14140) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 24744) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 12256) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 27940) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 38716) 
if /i "%LOCALHOST%"=="wenzheshang" (%KILL_CMD% 28280)
del "f:\Thinking\program\pareto_front\Workdata\Fluent_Python\2023-06-14_21-42\cleanup-fluent-wenzheshang-38716.bat"
