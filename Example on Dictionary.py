print("Example on Sets DSA using Python")
class carsClass:

    carsList = {"Toyota": 20000}

    def addingNewCar(self, name, price):
        if name in self.carsList.keys():
            print("Car Name Already exist")
        else:
            self.carsList[name] = price

    def displayList(self):
        print(self.carsList)


carsclass = carsClass()
# carsclass.addingNewCar("Toyota", 200000)
# carsclass.addingNewCar("Toyota1", 200000)
# carsclass.addingNewCar("Toyota", 200000)
# print(carsclass.addingNewCar("Toyota", 200000))
carsclass.addingNewCar("Toyota1", 200000)
carsclass.displayList()