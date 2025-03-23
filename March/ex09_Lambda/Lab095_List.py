# list - collection of items

# grocery list - butter , bread , banana , paneer :
# 10th marks - 90 , 91 , 92 , 78 , 56

my_list = [1, 2, 3]  # same type of data (int)
my_list2 = [1, True, "sai", 12.34]

print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[4])
# list index out of range

my_list[0] = "sai"
my_list[1] = "kumar"
my_list[2] = "kumar03"
print(my_list)

print("-----")

for item in my_list2:
    print(item)

    print("----")

    for i in range(1, 5):  # range ( start , stop -1)
        print(i)
        # range(1 ,5) -> returns list [1 , 2 , 3 , 4]
