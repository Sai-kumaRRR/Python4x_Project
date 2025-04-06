import os

full_path = os.getcwd()
print(full_path)
full_path_file = full_path + "/example.txt"
print(full_path_file)

# Read  the file.
file = open(full_path_file)  # fileNotError - no such file
except Exception as e:
print("file not found ,fix the path or create a file")
finally:
print("this code will be executed anyhow")
