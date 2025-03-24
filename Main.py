# Displays start message as the model can take a bit of time to load
# Only displays as main files to not mess with external projects
if __name__ == "__main__":
    print(f"Running: {__file__}\nThe model can take some time to load...\n")

# Checks the user's os to stop import errors
import os

# Quits if not on windows
if os.name != "nt":
    print(f"OS: {os.name} is not supported as this script requires windows-libraries and file paths.")
    input("Press enter to exit: ")
    os._exit(2)

import random
import time
import sys
import os

from Input import *

# OS-Specific file paths
PYTHON_FILES_DIRECTORY = "C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\RAG\\trt-llm-rag-windows-ChatRTX_0.4.0\\ChatRTXUI\\engine"
MODELS_DIRECTORY = "C:\\ProgramData\\NVIDIA Corporation\\ChatRTX"

# Adds the ChatRTX engine dir to system path for importing from
# Sys path is reset after program closes so does not change it permanently
sys.path.append(PYTHON_FILES_DIRECTORY)

# Imports the needed files from ChatRTX
from configuration import Configuration # type: ignore
from backend import Backend, Mode # type: ignore

def ChatRTX_CLI_Init():
    # Starts the LLM
    model = Backend(model_setup_dir = MODELS_DIRECTORY)
    model.init_model(model_id = "mistral_7b_AWQ_int4_chat")

    # Sets the state of the model [AI or RAG]
    model.ChatRTX(chatrtx_mode = Mode.AI)

    # Returns the model so it can be used
    return model

# Main function of this program
# Defined as a function so it is possible to call it in other projects
def ChatRTX_CLI_Main():
    # Enters try block to control program ending
    try:
        # Initialises the LLM and other resources
        model = ChatRTX_CLI_Init()

        # Creates the Query input controller
        user_input = QueryController()

        # Makes sure data is not cleared from the console without user knowing
        input("\nPress enter to the chat (Will clear the console): ")
        ClearConsole()

        # Main loop
        while True:
            # Gets answer from the LLM according to what the user inputted
            prompt = user_input.GetQueryFromUser()
            answer_stream = model.query_stream(query = prompt)
            
            # Makes it act as a single string
            answer = "".join(answer_stream) + "\n"

            # Displays to the console
            for char in answer:
                print(char, end = "", flush = True)

                # Stops whitespace taking time to display to the console
                if char != " ":
                    time.sleep(random.uniform(0.005, 0.009))

    # Catches CTRL + C and sends 0 which does not restart the program
    except KeyboardInterrupt:
        os._exit(1)

    # Catches any error and restarts
    except Exception as e:
        # Displays error
        print(f"An error occured: {e}")
        input("\nPress ENTER to restart program or CTRL + C to quit: ")

        # Error code 201 tells the batch file to restart the program
        os._exit(201)

# Only runs the main function if it is the starting file
if __name__ == "__main__":
    ChatRTX_CLI_Main()
