#  web automation
# page - you are going automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

        def log_confirm(self):
            if self.email == "saikumar143@gmail.com" and self.password == "Pass143":
                print("Allowed,Login Success")
            else:
                print("Login Failed")

          #  email = #Read from test data - excel , csv or ENV file

           # password = #Read from test data - excel . CSV or ENV file


            # vwo_obj = VwoLoginPage(email , password)

             # vwo_obj.login_confirm()

    vwo_obj = VWOLoginPage("saikumar143@gmail.com", "Pass143")
    vwo_obj.login_confirm()
