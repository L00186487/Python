'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo String Interpolation

One of the things we must do in many programs, is to open a file for reading or writing. 
There are four modes in which you can open a file: 
Read = “r” 
Write = “w” 
Append = “a” 
Read and write = “rw”

This code creates a log file and give you messages for each section which runs.
'''

my_filename = "logfile.txt"

try:
    with open(my_filename, "a") as file_handle:
        print(f"Writing a test line to {my_filename}")
        file_handle.write("Test line")
except IOError as err:
    print(f"IOError was {err}")
except EOFError as err:
    print(f"End of file error was {err}")
except OSError:
    print("OS Error")
except:
    print("General Error")
else:
    print("File created")
finally:
    print("Finishing up!")
    # close not needed because with statement
    # file_handle.close()