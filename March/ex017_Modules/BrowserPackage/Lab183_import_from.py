from browserPackge.OpenBrowser import start_browser
from browserPackge.CloseBrowser import stop_browser


def test_Case():
    start_browser()
    print("hello running TC")
    stop_browser()

    test_Case()