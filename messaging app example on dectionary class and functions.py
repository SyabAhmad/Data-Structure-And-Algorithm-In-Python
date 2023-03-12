class user:
    messageDict = {}
    isLogin = False # True
    def __init__(self, userName, pinCode):
        self.userName = userName
        self.pinCode = pinCode


    def isAuthintic(self):
        if self.userName == "de" and self.pinCode == 1234:
            self.isLogin=True

    def login(self):
        self.userName = input("Enter Your Name: ")
        self.pinCode = int(input("Enter Your PinCode: "))
        self.isAuthintic()



    def inputFromUSer(self):
        if self.isLogin == True:
            print("login Success")
            self.name = input("Enter Name of the Person: ")
            self.message = input("Type Your Message: ")
            self.messageDict[self.name] = self.message
            choice = input("type y for more messages and n for exit")
            if choice == "y":
                self.inputFromUSer()
            else:
                return
        else:
            print("Invalid Arguments: please Try Again")
            self.login()


    def outPutForUser(self):
        print(self.messageDict)


user1 = user("de Developer", 1234)
user1.login()
user1.inputFromUSer()
user1.outPutForUser()