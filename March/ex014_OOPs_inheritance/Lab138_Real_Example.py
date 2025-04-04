class BaseTest:

    def open_browser(self):
        print("starting the browser!")

        def read_from_excel(self):
            print("Read from excel ")

        def close_browser(self):
            print("close browser!")

            class Testcase1(BaseTest):

                def test_positive(self):
                    self.open_browser()
                    print("Test case p1 Executed!!!")
                    self.read_from_excel()
                    self.close_browser()

                    def test_negative(self):
                        self.close_browser()
                        print("Test case n1 Executed!!!")
                        self.close_browser()

            class Testcase2(BaseTest):

                def test_2(self):
                    self.open_browser()
                    print("Test case2 Executed !!!")
                    self.close_browser()

                    class TestCase3(BaseTest):

                        def test_3(self):
                            self.open_browser()
                            print("Test case p3 Executed !!!")
                            self.close_browser()
