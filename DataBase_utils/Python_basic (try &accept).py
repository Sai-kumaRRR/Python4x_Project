try:
    with open ("TestData.txt","r")as file:
        Content=file.read()
        print(Content)
except FileNotFoundError  as fnfr:
    print(fnfr)
#finally:
      # File.close()