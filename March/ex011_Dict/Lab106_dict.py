my_dict = {
    "name": "SAI",
    "age": "26",

    "role": "SDET",
    "experience": 3

}
print(my_dict)
print(my_dict["age"])

my_dict["role"] = "manual tester"
print(my_dict)

del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(key, " ->", value)

    print("age " in my_dict)
    print("role " in my_dict)
