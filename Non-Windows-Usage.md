# Not Using Windows or non Default Download Location?

This program was developed on windows but none of the code is OS-Specific. The only things that need to be changed in the code are 2 file paths which can be found at the top of Main.py:

1. PYTHON_FILES_DIRECTORY is where Configuration.py and Backend.py are located within the ChatRTX folder of Program Files
2. MODELS_DIRECTORY is where the models are stored in the ChatRTX folder of Program Data

The final thing that needs fixing is Run.bat, .bat files are exclusive to windows so you will have to run it via the command folder or create your own shell script if you are on a seperate OS. The only important part of the .bat file is this line:
```
"C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\env_nvd_rag\\Scripts\\python.exe" Main.py
```

The string is where Python is installed as part of ChatRTX. IMPORTANT: you cannot use a default python installation, it must be the version of python installed in ChatRTX.

You will also have to make a folder called "Chats" in the directory where you will be running the program.
