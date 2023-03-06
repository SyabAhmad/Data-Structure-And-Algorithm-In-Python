print("Flight Management System using Python Dictionary")

class flightManagementSystem:
    passportNumber = {}
    nameAndAge = {}

    def addingNewUser(self, passportID, passportName, userName, userAge):
        if passportID in self.passportNumber.values():
            print("Already Exist, try different One")
        else:
            self.passportNumber[passportName] = passportID
            self. nameAndAge[userName] = userAge
            print("User Added Succefully")

    def displayList(self):
        print(self.passportNumber)
        print(self.nameAndAge)

        # TO Display Keys and Values
        # for PassportID And CNIC ID
        print(self.passportNumber.keys())
        print(self.passportNumber.values())

        # for USer Name and AGe
        print(self.nameAndAge.keys())
        print(self.nameAndAge.values())


flightmanagementsystem = flightManagementSystem()

# flightmanagementsystem.addingNewUser(12345678, "CNIC", "De Developer", 23)
# flightmanagementsystem.addingNewUser(12345978, "CNIC", "De Developer", 24)
# flightmanagementsystem.addingNewUser(123458, "CNIC", "De Developer", 24)
# flightmanagementsystem.addingNewUser(123458, "CNIC", "De Developer", 24)
flightmanagementsystem.addingNewUser(123458, "CNIC", "De Developer", 24)
flightmanagementsystem.addingNewUser(12334523428, "Passport", "De Shah", 64)
flightmanagementsystem.displayList()