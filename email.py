import re
class Email:
    def __init__(self):
        print("Email class initialized")

    def valid_email(self):
        self.email = input("Enter your email: \n")
        self.result =re.search(r"[a-zA-Z0-9]+@(gmail)+\.com$",self.email)
        if self.result:
            print("Valid email")
        else:
            print("Invalid email")
            self.valid_email()

em = Email()
em.valid_email()
        