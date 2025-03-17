# Write  a program to take a user age and
# let him know if he can go the club
# 21

# Logic building formula

# step1

# user input i/p -> data type -> int
# o/p -> String -> user if he can go or not

# step 2. Rough logic (Brute force)

# ge >21 -> print can go
# age < 21 -> print can't go
#  step3 . write the logic
age = input("enter you age\n")
age = int(age)

if age >= 21:
    print("can go to club!")
else:
      print ("Can't go with this age")
# step 4. check for the edge cases.
# We should consider edge cases such as:
# Negative ages or extremely high values -> > 130

# step 5 . optimize the code .
