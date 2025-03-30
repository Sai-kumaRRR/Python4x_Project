# encapsulation
# Hide the data members( class , variables , instance variable)
# by using only the methods


def __init__(self):
    self.password = "sai"  # pubilc instance variable
    self.__password_secure = "pass143"  # private instance variable

    def change_password(self):
        print(self.password)

        object_ref = car()
        print(object_ref.password)
        print(object_ref.__password_secure)  # 'car' object has no attributes '__password'
