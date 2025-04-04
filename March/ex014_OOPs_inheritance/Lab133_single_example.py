# single inheritence

class Parent:
    gold = "2kg"

    def __init__(self):
        print("DC - parent")

        def BH2(self):
            print("BHK")

            class Child(Parent):

                def __init__(self):
                    print("DC - Child")

                    diamond = "Diamond"

                    def BHK3(self):
                        print("3BHK")

                        child_object = Child()
                        print(child_object.gold)
                        child_object.BHK2()

                        father_object_ref = Parent()
                        father_object_ref.BHK2()
                        # father_object_ref,BHK3()
