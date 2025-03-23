def add_before_ui_after_ui(func):

    def wrapper():
        print("before the running ui tc")
        print("start the browser")
        func()
        print("ending the running ui tc")
        print("quit the browser !")

        return wrapper()

    @add_before_ui_after_ui
    def test_ui():
        print(">> i will test ui")

