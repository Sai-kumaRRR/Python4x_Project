
class Father:

    def home(self):
        print("1BHK")


        class Sai(Father):

            def home(self):
              print("3BHK")


         s = Sai()
        s.home()

        f = Father()
        f.home()


