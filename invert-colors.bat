@echo off
rem SumatraPDF, -invert-colors batch file
set /p userin= Drop here :
start SumatraPDF.exe -invert-colors %userin%