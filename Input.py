import msvcrt
import os

# Easier way to clear the console
def ClearConsole():
    os.system("cls")

# Custom user input class
class QueryController:
    # Private member variables #
    __query = ""
    __length = 0
    __index = 0

    # Handles any key press that is more than one byte
    def __HandleMultiByteKeyPress(self, key):
        keyID = ord(key) # Numerical representation of the key

        match(keyID):
            case 75:
                if self.__index > 0:
                    # Moves the cursor to the left (\x1b[1D) is a special operation in the console
                    print("\x1b[1D", end = "", flush = True)
                    self.__index = self.__index - 1 # Updates the index

            case 77:
                if self.__index < self.__length:
                    # Moves the cursor to the right (\x1b[1C) is a special operation in the console
                    print("\x1b[1C", end = "", flush = True)
                    self.__index = self.__index + 1 # Updates the index

    # Handles any key press that is one byte
    def __HandleSingleByteKeyPress(self, key):
        keyID = ord(key) # Numerical representation of the key

        match keyID:
            case 18: # CTRL + R
                os._exit(201) # Tells the batch file to restart the process

            case 13: # Enter
                print()
                return True

            case 8: # Backspace
                # Checks it does not remove from ordinary console output
                if self.__index == 0:
                    return False

                self.__length = self.__length - 1
                self.__index = self.__index - 1

                # Removes the character from the query
                self.__query = self.__query[:self.__index] + self.__query[self.__index + 1:]

                # Prints new query to the console
                print(f"\rQuery: {self.__query} \x1b[1D", end = "", flush = False)

                # Puts the cursor back to where it was
                for i in range(self.__length - self.__index):
                    print("\x1b[1D", end = "", flush = False)

                # Updates the console
                print("", end = "", flush = True)

            case _: # Default case
                self.__length = self.__length + 1 # Updates the length

                # Decodes the key
                key = key.decode("utf-8")[0]

                # Adds the key to the string and displays to the screen
                self.__query = self.__query[:self.__index] + key + self.__query[self.__index:]
                print(f"\rQuery: {self.__query}", end = "", flush = False)

                # Puts the cursor back to where it was
                for i in range((self.__length - self.__index) - 1):
                    print("\x1b[1D", end = "", flush = False)

                # Updates the console
                print("", end = "", flush = True)

                self.__index = self.__index + 1 # Updates the index

        # Tells the caller not to return the query
        return False

    #
    def GetQueryFromUser(self):
        # Resets member variables #
        self.__query = ""
        self.__length = 0
        self.__index = 0

        print("Query: ", end = "", flush = True)

        while True:
            # Checks if a key has been pressed
            if msvcrt.kbhit():
                # The first byte of the key that has been pressed
                # Most keys are one bit but some special characters are more
                key_b1 = msvcrt.getch()

                # If the first byte is equal to '\xe0' it means it is more than one byte
                # This requires different logic so it is handled by a different function
                if key_b1 == b'\xe0':
                    self.__HandleMultiByteKeyPress(msvcrt.getch())

                else:
                    # If this returns true it means the ENTER key has been pressed so the input is finish
                    if self.__HandleSingleByteKeyPress(key_b1):
                        return self.__query