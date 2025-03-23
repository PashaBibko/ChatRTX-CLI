@echo off

REM Creates a folder to store the chats
mkdir Chats

REM Lable for start of loop
:loop
	REM Clears the screen for clearer output
	cls

	REM Runs the ChatRTX CLI
	"C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\env_nvd_rag\\Scripts\\python.exe" Main.py

	REM Checks if it returned restart exit code
	if %ERRORLEVEL% == 201 (
		goto loop
	)
