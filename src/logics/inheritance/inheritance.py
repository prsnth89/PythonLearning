class Vehicle:
      wheels=None #declar common variables
      name=None
      year=None
      speed=None
      def noOfWheels(self,noOfWheels):
           self.wheels=noOfWheels #assign to current variable using self.
           return self.wheels

      def nameAndModel(self,name,year):
            self.name=name
            self.year=year
            return print(f'My vehicle name is {self.name}'
                         f' and year of manufacturing is {self.year}')
      def maxSpeed(self,speed):
          self.speed=speed
          return print(f'Vechicle speed of {self.name} is {self.speed}')
      
      def getMaxSpeedOfVehicle(self):
            print(f'Max speed of vehicle {self.name}  is {self.speed}')
      def __init__(self,name,vehicleName):
            self.nameAndModel(name, vehicleName)
      

class BMW(Vehicle):  #achieve inheritance using (Vehicle)
      def drivingExperienceOfBMW(self):
            print("BMW is the best car which i have travelled")
class Pulsar(Vehicle):
      def drivingExperienceOfPulsar(self):
            print ("Best bike to enjoy travel")

class testVehicle:
      testBMW=BMW("BMW",2018) #calling vehicle function and settingup the value in testbmw instance
      testBMW.wheels=4
      print("No of wheels of BMW car is ---",{testBMW.wheels})
      testBMW.maxSpeed(300)
     # testBMW.getMaxSpeedOfVehicle()

      testPulsar = Pulsar("Pulsar",2010) #calling vehicle function and settingup the value in testbmw instance
      testPulsar.wheels = 2
      print("No of wheels of Pulsar bike is ---", {testPulsar.wheels})
      testPulsar.maxSpeed(150)
    #  testPulsar.getMaxSpeedOfVehicle() --moving to forloop

      for allVehicles in [testBMW, testPulsar]:
            print("-----Entering into for loop------")
            allVehicles.getMaxSpeedOfVehicle()  #iterating objects and getting its values
      