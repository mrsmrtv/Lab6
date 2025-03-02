import os

file_path = input()

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print("Deleted")
    else:
        print("Permission denied")
else:
    print("File does not exist.")