student_information1 ={
    "name": "SAI",
  #  "age": 26 ,
  "age": 48,
"address": {
    "home_address": "vskp",
    "office_address": "pune"
}

}

student_information2 = {
    "name": "abhi",
    #"age" : 34,
    "age" : 54 ,
    "address": {
        "home_address": "bsp",
        "office_address": "durg"
    }
    
}

student_list = [student_information1,student_information2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list["address"]["office_address"])
# print(student_list)
# print(student_list)