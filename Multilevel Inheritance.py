# Multilevel Inheritance
 
class GrandFather:
    def ownHouse(self):
        print("Grandpa House")
 
 
class Father(GrandFather):
    def ownBike(self):
        print("Father's Bike")
 
 
class Son(Father):
    def owncycle(self):
        print("Son's cycle")
 
 
o = Son()
o.ownHouse()
o.ownBike()
o.owncycle()




        