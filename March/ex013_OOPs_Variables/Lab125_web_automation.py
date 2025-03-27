# Web automation - selenium
# page - you are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg, ):
        self.email = email_arg
        self.password = passw

    def login_confirm(self):
        if self.email == "saikumar@143gmail.com" and self.password == "pass143":
            print("Allowed, LoginSuccess")


        else:
            print("Login Failed")

        #  email = i# Read from excel file or env file
        # password = #Read from excel file or env file

        # vwo_obj = VWOLoginPage( email , password)
        # vwo_obj. login_confirm()

        sai = VWOLoginPage("saikumar@143gmail.com", "Pass143")
        sai.login_confirm()
