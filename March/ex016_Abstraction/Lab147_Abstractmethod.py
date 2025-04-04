from abc import ABC, abstractmethod
class Father(ABC):

    def __init__(self,name):
        self.name = name


        @abstractmethod
        def loan(self):
            pass


        class Son(Father):

            def loan(self, sai_obj=None):
                print("1L given")

                Sai_obj = Son("sai")
                sai_obj.loan()