try:
    num1 = int(input("enter a number 1\n"))
    num2 = int(input("enter a number 2\n"))
    result = num1/num2     # option - 1
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)



    try:
        num1 = int(input("enter a number 1\n"))
        num2 = int(input("enter a number 2\n"))
        result = num1 / num2     # option -2
    except Exception as e:
        print(e)