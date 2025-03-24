@echo off

REM Creates the folder where the chats are stored
mkdir Chats

:loop
	cls

	REM Runs the python script via the python installation downloaded via ChatRTX
	REM Using a different installation of python will cause issues
	"C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\env_nvd_rag\\Scripts\\python.exe" Main.py

	REM Exit code 201 represents the restart exit
	if %ERRORLEVEL% == 201 (
		goto loop
	)
