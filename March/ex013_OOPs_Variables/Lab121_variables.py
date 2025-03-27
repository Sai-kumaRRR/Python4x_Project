a = 10

class Person:
    b = 11 # Instance - belong to class

    def print_info(self):

        c= 29 #  local variables

        print(c)
        print(self.b)
        a = "Hello"
        print(a)

        object_ref = Person()
        object_ref.print_info()
