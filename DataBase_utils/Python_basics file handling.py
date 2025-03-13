#File handling
#how to read a Text,and to writing  it using python code

#function
# open("file_name",'mode")

#mode
#"r" for reading (default)
#"w" for writing (creates a new file or truncates an existing one )
#"a" for appending
#"b" for binary mode. zoom .exe -binary
#"+" for updating (reading and writing)

#Read and write content
# read a file
#Reading Entire Content: = file _objet.read()
# line =file_object.readline() for a single line
# lines =file_object.read lines() for all lines in a list

# close the file



file =open("test data.txt","r")
content = file . read()
print(content)
file.close()