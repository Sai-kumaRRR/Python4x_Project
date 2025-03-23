# write a program to calculate even and odd

# def find _even _odd (num):
# if num %2 == 0:
# print("even ")
# else:
# print("odd")


# find_even_odd(5)

n = int(input("enter a num\n"))
check_even_odd = lambda num: "even" if num % 2 == 0 else "odd"

# print(check_even_odd(17))
#print(check_even_odd(10))
print(check_even_odd(n))