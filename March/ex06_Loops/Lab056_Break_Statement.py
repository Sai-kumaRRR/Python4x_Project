for i in range(0, 10):  # 0 to 9 , times -> 10
    print(i)
    if i == 5:
        break
        # | i | condition | o/p = 0
        # | 0 |  0 == 5 -> false | o/p = 0
        # | 1 |   1 == 5 -> false | o/p =1
        # | 2 | 2 == 5 -> false | o/p = 2
        # | 3 | 3 == 5 -> false | o/p = 3
        # | 4 | 4 == 5 -> false | o/p =  4
        # | 5 | 5 ==5 -> true | o /p = BREAK  out of  for loop
