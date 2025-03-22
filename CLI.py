print("Importing...")

import msvcrt
import sys
import os

sys.path.append("C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\RAG\\trt-llm-rag-windows-ChatRTX_0.4.0\\ChatRTXUI\\engine")

from configuration import Configuration
from backend import Backend, Mode

print("Initialsing...")

def GetPromptFromUser():
    print("Query: ", end = "", flush = True)
    query = ""

    # Gets keypresses from the console
    while True:
        if msvcrt.kbhit():
            # Decodes the key and gets the ASCII value
            key = msvcrt.getch().decode("utf-8")[0]
            keyID = ord(key)

            # Checks for commands
            match keyID:
                # case 18: # CTRL + R
                    # os.execv(sys.executable, [sys.executable] + sys.argv)

                case 13: # Enter
                    print()
                    return query

                case 8: # Backspace
                    # Removes last char from console
                    print("\b \b", end = "", flush = True)

                    # Removes last char from the query
                    query = query[:-1]

                    pass

                case _: # Default case
                    query = query + key
                    print(key, end = "", flush = True)

print("Starting model...")
model = Backend(model_setup_dir = "C:\\ProgramData\\NVIDIA Corporation\\ChatRTX")
model.init_model(model_id = "mistral_7b_AWQ_int4_chat")

status = model.ChatRTX(chatrtx_mode = Mode.AI)

try:
    while True:
        prompt = GetPromptFromUser()

        # Gets answer from the LLM
        answer = model.query_stream(query = prompt)

        # Prints the answer to the console
        for part in answer:
            print(part, end = "")

        print(flush = True) # Just for nicer formating

except KeyboardInterrupt:
    pass
