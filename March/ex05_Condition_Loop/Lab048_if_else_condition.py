#Problem to find the max between two.

# logic building formula


#1. user inputs -> two integers
# 2. o/p -> int 1 which ever is greater max number it will return.
# 31.4 or 45.65 - float


num1  = float(input("enter the num1\n"))
num2 = float(input ("enter the num2\n"))

if num1 >= num2:
    print("max is ", num1)

else:
    print("max is ", num2)

    # edge cases - num1 == num2 -> handled .