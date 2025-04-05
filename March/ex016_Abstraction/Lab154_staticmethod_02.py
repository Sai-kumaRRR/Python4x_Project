class ExcelReader:
    def read_from_excel(self):
        print("Reading from excel")


        class MYSQLDBConnection:

            @staticmethod
            def readyMySQLFile():
                print("Reading from MySQL")


                class TC1:
                    static_var = 10

                    @staticmethod
                    def testcase():

                        MYSQLDBConnection.readyMYSQLFile()
                        ExcelReader.read_from_excel()
                        print(TC1.static_var) # shared among all instance of the class


                        TC1.testcase()