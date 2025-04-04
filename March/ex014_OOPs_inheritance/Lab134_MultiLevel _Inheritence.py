# MultiLevel - inheritance.

class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")

        class Father(GrandFather):
            diamond = "22 karat"


def bhk2(self, father=None):
    print("2BHK")

    class Son(father):
        btc = "1BTC"

        def bhk3(self):
            print("3BHK")

            s = Son()
            print(s.gold)
            print(s.diamond)
            print(s.btc)
       
            f = father()
            # print(f.btc)
            print(f.gold)
