class Car():

    def __init__(self,builder,model,released_year):
        self.builder=builder
        self.model=model
        self.released_year=released_year


    def display_info(self):
        print( self.builder+" made this car named"+self.model+" in this"+self.released_year)


class Electric_Car(Car):

    def __init__(self, builder,model, released_year, battery_capacity):
        super().__init__(builder,model,released_year)
        self.battery_capacity=battery_capacity


    def display_battery(self):
        print("the battery capacity is:"+self.battery_capacity)
        super().display_info()




tesla= Electric_Car("tesla","Roadroster","2016","2500 Ahr")

tesla.display_battery()


