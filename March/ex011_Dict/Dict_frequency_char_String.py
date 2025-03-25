# Frequency of characters in a string

# write a program to count the frequency of each character in a given string.

String = "Automation "
String = input("enter the input e.g automation")

# { {a : 2 , u :1 , t: 2 , o: 2 , m: 1 , n :1 , i : 1 , n : 1 }}

char_char = {}
# logic building
# I/P - string e.g automation
# O/P -> dict # { a : 2 , u : 1 , t : 2 , o : 2 , m : 1 , n : 1 , i : 1 , n : 1 }

for char in String:
    char_count[char] = char_count.get(char, 0)+1

    print(char)
