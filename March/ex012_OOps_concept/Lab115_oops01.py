class Person:
 #Attributes - What you have?

id = None
name = None
age = None
email = None
height = None
gender = None
phone_no = None
address = None


# Behaviour - what you can do?

def talk(self):  # self - this , self will be first argument .
    print("i can talk")

    def sleep(self, name):  # arg with no return
        print("I am a method!!")
        print("Sleep",name)


def sleep2(self , name): # arg with return
    print("I am a method!!")
    return None

def walk(self):
    print("i am walking")

    def walk_return(self): # no arg with return
        return("I am walking")