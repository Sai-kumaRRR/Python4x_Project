# Hierarchical inheritance


def Lucky():
    pass


class father:

    def Bhk1(self):
        print("1BHK")

        class Sai(father):

            def BHK2(self):
                print("2BHK")

                class sonu(father):

                    def BHK3(self):
                        print("3BHK")

                        class lucky(father):

                            def no_house(self):
                                print("NO house")

                                sai = Sai()
                                sai.BHK1()
                                sai.BHK2()

                                sonu = Sonu()
                                sonu.BHK1()
                                sonu.BHK3()
                                
                                # sonu.BHK2()    # this belong to sai
                                
                                l = Lucky()
                                l.BHK1() # only father house
