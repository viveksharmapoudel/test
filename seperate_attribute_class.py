from inheritanceCarElectricCarExample import Car

class Battery():
    def __init__(self, battery_size=70):

        self.battery_size=battery_size


    def describe_battery(self):
        print(str(self.battery_size)+" is the battery capacity")




class ElectricCar(Car):

    def __init__(self, builder, model, released_year):
        super().__init__(builder, model, released_year)
        self.battery =Battery()




tesla= ElectricCar("tesla","roadRoster","2016")


tesla.battery.describe_battery()


