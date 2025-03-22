print("Importing...")

import msvcrt
import sys
import os

sys.path.append("C:\\Program Files\\NVIDIA Corporation\\ChatRTX\\RAG\\trt-llm-rag-windows-ChatRTX_0.4.0\\ChatRTXUI\\engine")

from configuration import Configuration
from backend import Backend, Mode

print("Initialsing...")

print("Starting model...")
model = Backend(model_setup_dir = "C:\\ProgramData\\NVIDIA Corporation\\ChatRTX")
model.init_model(model_id = "mistral_7b_AWQ_int4_chat")

status = model.ChatRTX(chatrtx_mode = Mode.AI)

try:
    while True:
        # Gets query from user
        answer = model.query_stream(query = input("Query: "))

        # Prints the answer to the console
        for part in answer:
            print(part, end = "")

        print() # Just for nicer formating

except KeyboardInterrupt:
    pass
