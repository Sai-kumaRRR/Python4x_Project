# Remove duplicate values from a dictionary .

my_dict = {"a ": 1 , "b": 2, "c": 3, "d ": 5}

# output: {'a': 1 , 'b': 2 , 'd': 5}
unqiue_value = set()

result = set()

result = ()
for key, value in my_dict.items():
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

        print(result)
