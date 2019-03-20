class Vehicle:

     def __init__(self, name,type,model):
         self.name = name
         self.type = type
         self.model = model

     def run(self):
         print(self.name, " ", self.model, " is running")


class Motorcycle(Vehicle):    # Inheritance
    def intro(self):
        print(self.name," is a motor bike")

a = Vehicle("BMW","Sedan","Series 3")
a.run()
b = Motorcycle("Harley Davidson", "Motor Bike", "D300")
b.run()
b.intro()
