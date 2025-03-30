#  web auto automation
# page - you are going automate
import os

from dotenv import load_dotenv


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

        def log_confirm(self):
            if self.email == "saikumar143@gmail.com" and self.password == "Pass143":
                print("Allowed,Login Success")
            else:
                print("login failed")

                load_dotenv
                email = os.getenv("EMAIL")

                password = os.getenv("PASSWORD")

                print(email, password)

            vwo_obj = VWOLoginPage(email, password)
            vwo_obj.login_confirm()
