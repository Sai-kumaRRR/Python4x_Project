# Argument + return type



def sum_of_two(a , b):
    return a+b
result = sum_of_two(4 , 56)
print(result)

def sum_of_two_number_with_default(num1 = 100, num2 =200):
    print("i will sum the two numbers!")
    return num1 + num2

result = sum_of_two_number_with_default(num1 =34 ,num2 = 34)
print(result)
result = sum_of_two_number_with_default()
print(result)