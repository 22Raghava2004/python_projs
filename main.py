import os
file_path="script\\test.txt"
if os.path.exists(file_path):
    print(f"the file location exist {file_path}")
else:
    print("dosnt exist")