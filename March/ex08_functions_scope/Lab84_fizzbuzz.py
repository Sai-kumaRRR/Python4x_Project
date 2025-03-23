# write a program that prints numbers from 1 to 100.
# however , for multiple of 3 , print fizz instead of the numbers.
# and for multiple of 5 , print "buzz . for numbers that are
# multiple of both 3 and 5 print fizzbuzz (for , if)

for number in range(1 , 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 ==0:
        print("buzz")
    elif number % 3==0:
        print("fizz")
    else:
        print(number)