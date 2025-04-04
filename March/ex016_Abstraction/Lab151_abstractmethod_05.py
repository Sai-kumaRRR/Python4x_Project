from abc import ABC, abstractmethod


class ExcelReader(ABC): ...


class Browser(ExcelReader):

    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

    class Hidden(Browser):
        @abstractmethod
        def hidden(self):
            print("Hidden")

            class TC():
                def startBrowser(self):
                    print("strating")

                    def stopBrowser(self):
                        print("stop")
