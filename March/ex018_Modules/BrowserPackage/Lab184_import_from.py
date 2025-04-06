import dataclasses

from ex018_Modules.BrowserPackage.CloseBrowser import stop_browser
from ex018_Modules.BrowserPackage.OpenBrowser import start_browser




class TestCase:

    def test_case(self):
        start_browser()
        print("hello running tc")
        stop_browser()

        obj_tc = TestCase()
        obj_tc.Case()
