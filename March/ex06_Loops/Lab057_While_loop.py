for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        print(" no o/p")

    # /  i  /  condition  / o/p
    # /  0 / 0 ==6 -> false / o/p ->  no  o/p
    # /  1 / 1 ==6 -> false /  o/p -> no o/p
    # /   2 / 2 ==6  -> false  / o/p -> no o/p
    # /  3 / 2 == 6 -> false / o/p -> no  o/p
    # / 4 / 4 == 6 -> false / o/p -> no  o/p
    # / 5 / 5 ==6 -> false / o/p -> no o/p
    # / 6 / 6 == 6 -> true  / o/p ->  6
    # / 7 / 7 ==6  -> false / o/p ->  no o/p
    # / 8 / 8 ==6 -> false / o/p -> no  o/p
    # / 9 / 9 ==6 -> false / o/p -> no o/p
