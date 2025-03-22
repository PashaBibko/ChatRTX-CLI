# Script I use for testing #
# Not used for the main program #

import msvcrt

# Gets keypresses from the console
try:
    while True:
        if msvcrt.kbhit():
            # Decodes the key and gets the ASCII value
            key = msvcrt.getch().decode("utf-8")[0]
            keyID = ord(key)

            # Displays to the console
            print(f"Key pressed: {key}, ID: {keyID}")

except KeyboardInterrupt:
    pass
