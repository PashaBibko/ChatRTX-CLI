@echo off

REM Lable for start of loop
:loop
	REM Clears the screen for clearer output
	cls

	REM Runs the ChatRTX CLI
	"C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\env_nvd_rag\\Scripts\\python.exe" CLI.py

	REM Checks if it returned restart exit code
	if %ERRORLEVEL% == 1 (
		goto loop
	)
