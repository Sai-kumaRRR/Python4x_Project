def time_decorator(func):
    def wrapper():
        end_time = time.time()
        print(end_time)
        print("total time take by func -> ", end_time - start_time)
        return wrapper()

    @time_decorator
    def test_ui_1():
        print("add a function , time taken by this function")
        time.sleep(2)

        @time_decorator
        def test_ui_2():
            print("add a function , time taken by this function")
            time.sleep(5)
