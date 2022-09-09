#Nikola Petreski
#M03 Lab
#This program is designed to ask a user for information about their vehicle, and return that information in a report format.

#DESCRIPTION OF VARIABLES
#Vehicle - This is a super class that contains the attribute for the type of vehicle.
#Automobile- This class inherits from vehicle and enables the user of different attributes
#year - This is the vehicle's year.
#type- This is the vehicle's type.
#make- This is the vehicle's make.
#doors- This is the amount of doors the vehicle has.
#model- This is the model of the vehicle.
#roof- This represents what kind of roof the vehicle has.

class Vehicle():
    def __init__ (self, type):
        self.type=type
    
class Automobile(Vehicle):
    def __init__(self,year,make,model,doors,roof):
            super().__init__(type)
            self.year=year
            self.make=make
            self.model=model
            self.doors=doors
            self.roof=roof


type = str(input("What type of vehicle do you have?: "))
year = int(input("What is your vehicle's year?: "))
make = str(input("What make is your vehicle?: "))
model = str(input("What what model is your vehicle?: "))
doors = int(input("How many doors does your vehicle have?: "))
roof = str(input("Does your vehicle have a sun roof or a solid roof?: "))

print(f"Vehicle type: {type}")
print(f"Year: {year}")
print(f"Make: {make}")
print(f"Model: {model}")
print(f"Number of doors: {doors}")
print(f"Type of roof: {roof}")