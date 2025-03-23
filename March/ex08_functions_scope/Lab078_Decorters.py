def add_security(func):
    def warpper():
        print("1. before the function is called .")
        print("2.add helmet , dashcash , gloves , knee , guards , license")

        func()  # driving_scooty ()
        print("3. after function is called")
        print("4 . secure driving , leave all the items")

        return wrapper()

    @add_security
    def drive_ola_scooter():
        print("ola")

        @add_security
        def driving_scooty():
            print("normal function!!!")
            print("i am driving a scooty")
