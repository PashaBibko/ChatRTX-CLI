# Displays start message as the model can take a bit of time to load
# Only displays as main files to not mess with external projects
if __name__ == "__main__":
    print(f"Running: {__file__}\nThe model can take some time to load...\n")

import random
import msvcrt
import time
import sys
import os

# Adds the ChatRTX engine dir to system path for importing from
# Sys path is reset after program closes so does not change it permanently
sys.path.append("C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\RAG\\trt-llm-rag-windows-ChatRTX_0.4.0\\ChatRTXUI\\engine")

# Imports the needed files from ChatRTX
from configuration import Configuration
from backend import Backend, Mode

# Custom user input function
# Allows for commands like CTRL + R
# Works like input()
def GetPromptFromUser():
    # Simulates input() function
    print("Query: ", end = "", flush = True)
    
    # Initialises local variables
    query = ""
    length = 0
    index = 0

    # Gets keypresses from the console
    while True:
        # Checks if a key on the keyboard has been pressed
        if msvcrt.kbhit():
            # Gets the last key pressed
            key = msvcrt.getch()

            # Checks for the escape sequence
            # This means it is a special key
            if key == b'\xe0':
                key = msvcrt.getch() # Gets the second byte in the sequence
                keyID = ord(key) # Gets the numerical ID of the key

                # Finds the correct logic for the key
                match keyID:
                    case 75:
                        if index > 0:
                            # Moves the cursor to the left (\x1b[1D) is a special operation in the console
                            print("\x1b[1D", end = "", flush = True)
                            index = index - 1 # Updates the index

                    case 77:
                        if index + 1 < length:
                            # Moves the cursor to the right (\x1b[1D) is a special operation in the console
                            print("\x1b[1D", end = "", flush = True)
                            index = index + 1 # Updates the index

                    case _:
                        pass

            # Less special keys
            else:
                # Gets the numerical ID of the key
                keyID = ord(key)

                # Checks for commands
                # Else adds the character to the query
                match keyID:
                    case 18: # CTRL + R
                        os._exit(201) # Tells the batch file to restart the process

                    case 13: # Enter
                        print()
                        return query

                    case 8: # Backspace
                        # Checks it does not remove from ordinary console output
                        if index == 0:
                            continue

                        length = length - 1
                        index = index - 1

                        # Removes the character from the query
                        query = query[:index] + query[index + 1:]

                        # Prints new query to the console
                        print(f"\rQuery: {query} \x1b[1D", end = "", flush = False)

                        # Puts the cursor back to where it was
                        for i in range(length - index):
                            print("\x1b[1D", end = "", flush = False)

                        # Updates the console
                        print("", end = "", flush = True)

                        pass

                    case _: # Default case
                        length = length + 1 # Updates the length
                        index = index + 1 # Updates the index

                        # Decodes the key
                        key = key.decode("utf-8")[0]

                        # Adds the key to the string and displays to the screen
                        query = query + key
                        print(f"\rQuery: {query}", end = "", flush = True)

# Main function of this program
# Defined as a function so it is possible to call it in other projects
def ChatRTX_CLI_Main():
    # Enters try block to control program ending
    try:
        # Starts the LLM
        model = Backend(model_setup_dir = "C:\\ProgramData\\NVIDIA Corporation\\ChatRTX")
        model.init_model(model_id = "mistral_7b_AWQ_int4_chat")

        # Sets the state of the model [AI or RAG]
        status = model.ChatRTX(chatrtx_mode = Mode.AI)

        # Main loop
        while True:
            # Gets answer from the LLM according to what the user inputted
            answer_stream = model.query_stream(query = GetPromptFromUser())
            
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
        input("\nPress enter to restart program: ")

        # Error code 201 tells the batch file to restart the program
        os._exit(201)

# Only runs the main function if it is the starting file
if __name__ == "__main__":
    ChatRTX_CLI_Main()
