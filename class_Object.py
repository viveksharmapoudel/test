

class Dog:


    def __init__(self, name,age):
        self.name=name
        self.age=age


    def roll_over(self):

        print( self.name +" is rolling over")


    def sit_down(self):

        print(self.name + " your age is "+self.age+ " sit down")



dog_name= input("enter the dog_name")
dog_age=input("enter the dog age")


dog= Dog(dog_name,dog_age)

print(dog.name)

dog.roll_over()

dog.sit_down()

