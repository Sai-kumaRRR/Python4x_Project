# Dictionary from two lists


keys = ["name", "role", "experience"]
values = ["aman", "SDET", 3]

my_dict = dict(zip(keys, values))
print(my_dict)

# merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 4, "d": 5}

merged_dict = dict1 | dict2
print(merged_dict)
print(merged_dict.get("a"))
