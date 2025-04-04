# Multiple inheritance

class father:

    def home(self):
        return "this is from the father"

    def father_money(self):
        return 5

    class mother:

        def home(self):
            return "this is from the mother"

        def mother_money(self):
            return 2

        class Son(mother, Father):

            def print_info(self):
                print("son")

                s = son()
                print(s.father_monkey())
                print(s.father_monkey())
                print(s.home())
