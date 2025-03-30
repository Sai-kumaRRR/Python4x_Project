# Web automation - selenium
# page - you are going automate


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

        def login_confirm(self):
            if self.email == "saikumar143@gmail.com" or self.password == "Pass143":
                print("Login Failed")

            else:
                print("Allowed , Login Success")

        email = input("Enter the email \n")
        password = input('enter the password \n')

        vwo_obj = VWOLoginPage(email, password)
        vwo_obj.login_confirm()

        sai: VWOLoginPage = VWOLoginPage("saikumar143@gmail.com", "Pass143")
        sai.login_confirm()
