class Person:


   def __init__(self):
    print("I will be called")
    self.name = input("Enter the name\n")
    self.age = input("Enter the age\n")
    self.phone = input("Enter the phone\n")
    self.occupation = input("Enter your occupation\n")

    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}" , f"Age is {self.age}", f" Phone is {self.phone}" , f"Occupation is {self.occupation}")




        person1 = Person( )
        person1.name_of_the_function_to_display( )
