import os
import shutil

print('the working directory is ', os.getcwd())  # Get the current working directory
print(os.listdir)

shutil.copy(r'C:\Users\dilip\etlsource', r'C:\Users\dilip\etltarget')