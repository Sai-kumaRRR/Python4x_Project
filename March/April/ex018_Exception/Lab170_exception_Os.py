import os

print(os.getcwd())
# returns the current directory .

# list files in the current directory
file = os.listdir('/users/sai/py charm projects/pytab5xlearning')
print('f files in current directory:{files}')

# create a new directory
 #os.mkdir("test2")

 # check if a file exists
 file_exist = os.path.exists("sai.txt")
 print(file_exist)


print(os.name) # nt == microsoft