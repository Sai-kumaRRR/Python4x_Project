class OldBrowser:

    def start_browser(self):
        print("IE browser is starting")

        def stop_browser(self):
            print("IE browser is closing")

            class Chrome(OldBrowser):

                def start_browser(self):
                    super().start_browser()  # parent start browser also.
                    print("better chrome browser is starting....")

                    def stop_browser(self):

                        print("Better chrome browser  is stopping....")

                    pass

                obj_ref = Chrome()
                obj_ref.start_browser()
                obj_ref.stop_browser()
