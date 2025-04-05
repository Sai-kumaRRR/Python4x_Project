class BankAccount:

    def __init__(self, balance, acc_number):
        self.__balance = balance
        self.acc_number = acc_number

        class ICICI(BankAccount):

            def withdraw(self):
                print("yes")

                @abstractmethod
                def loan(self):
                    pass

                @astaticmethod
                def call_customer_care:
                    print("Calling")
