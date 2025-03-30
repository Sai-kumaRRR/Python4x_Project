# Encapsulation
# Hide the data members(class , variables , instance variables)
# by using only the methods.


class car:
    def __init__(self):
        self.passwoed = "sai" # public variable
        self.__password_secure = "pass143" # private instance variable


        def change_password(self):
            self.__password_secure ="456"


            object_ref = car()
            print(object_ref.password)

            print("---")


            print(object_ref.__password_secure)
            object_ref.change_password()
            print(object_ref.__password_secure) # 'car' object has no attribute '__password'

