print(" ---- start of the program")
try:
    a = int(input("enter the num1"))  # value error : invalid literal for int()
    b = int(input("enter the num2"))
    c = a / b  # zero division error :  division by zero
    print("result div is", c)

except Exception as e:
    print(e)

    print("----End of the program")

    # try and except
