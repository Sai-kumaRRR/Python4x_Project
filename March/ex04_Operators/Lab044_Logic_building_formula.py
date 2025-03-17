# task for the today
# take a 3 input from the user
# perform the sub , sub , mul and div

# logic building formula

# 1 - i/p , o/p
# taking there inputs from the user
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
num3 = float(input("enter the third  number:"))

# performing operators
sub_result = num1 - num2 - num3  # subtracting second number from first
sum_result = num2 + num1 + num3  # sub third number from second
mul_result = num1 * num2 * num3  # multiplying all three numbers
div_result = (num1 / num2 / num3)

print(sub_result)
print(sum_result)
print(mul_result)
print(div_result)
