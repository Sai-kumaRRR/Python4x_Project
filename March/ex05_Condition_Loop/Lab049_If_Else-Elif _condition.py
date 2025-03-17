# problem find the max between 3 numbers

# logic building

# user inputs - num1 , num2 , num3 -> int
# O/p -> int or String with max number

# logic ? If else - 1 condition,
# syntax
# if condition 1:
#  print("do 1")
# elif condition 2:
# print ("do 2")
# elif condition 3:
# print (" do 3:")
# else:
# print (" do for else")

num1 = int(input("enter the num1\n"))  # 5 , # 10
num2 = int(input("enter the num2\n"))  # 3 , # 12
num3 = int(input("enter the num3\n"))  # 2 , # 11

# 5 >3  and 5 > 2 -> 5

# num1  > num2 and num 1> num 3 -> num1


# 12 > 10  and 12 >> num1 and num2 > num3 -> num2

# num3
if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)

else:
    print("Max is", num3)
