'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: A first programme

Bring together previous examples

The following script determines the operating system and prints a message based on the result. 
If the script is imported as a module, it prints a different message indicating that it's being called by another script
'''

import platform 

def detect_os()->str:
    # Detect the OS in use
    return platform.system()


if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    elif my_os == "cygwin":
        print("Your Apple system is MacOS")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        print(f"Unidentified system = {my_os}")
else:
    print(f"This module is called {__name__} and is being called by another script")