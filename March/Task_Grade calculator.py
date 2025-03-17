# grade calculator
# write a program that calculates and display the letter grade
# for a given numerical score (e.g , a , b , c , d  , or f)
# based on the following grading scale

# a : 90-100
# b: 80 -89
# c: 70 - 79
# d: 60- 69
# f: 0-59


# logic building formula
# 1 -> user inputs ->  score or marks -> int
# 2 -> o/p -> str -> a or b
score = int(input("enter your score\n"))

# score >= 90 and score <=100 -> "A"
# score >= 80 and score <=89 -> "B"

if score >= 90 and score <= 100:
    print(" you grade is", "A")
elif score >= 80 and score <= 89:
    print("you grade is", "B")
elif score >= 70 and score <= 79:
    print(" you grade is", "C")
elif score >= 60 and score <= 69:
    print("you grade is", "D")
elif score >= 100:
    print("you are superman!!, you can't get a grade!! 0:")

else:
    print("you grade is", "F")
