def print_mul_arguments(*args):


# *args -> List
for i in args:
    print(i)

    print_mul_arguments("sai")
    print_mul_arguments("sai", "sonu", "omkar")

    print_mul_arguments("sai", 10, True, False, "sai")
