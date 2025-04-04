# How to create a class?

class Father:
    key = "2BHK"


    def car(self):
        print("father has a car -> alto")
        print(self.key)


        class Son:
            key2 = "3BHK"

            def suv(self):
                print("MG Hector , black")
                print(self.key2)

                father_obj = Father()
                father_obj.car()

                son_obj = Son()
                son_obj.suv()
