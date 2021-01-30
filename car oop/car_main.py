class Car:

    wheels = 4 

    def __init__(self,manu, current_gear, max_speed, current_speed):
        self.manu = manu
        self.current_gear = current_gear
        self.max_speed = max_speed
        self.current_speed = current_speed

    def changeGear(self, current_gear):
        self.current_gear = current_gear 
    def speedUp(self):
        print(self.current_speed*2)
    def slowDown(self):
        print(self.current_speed-10)


c1 = Car('Bmw', 2, 141, 34)
c2 = Car('Golf', 1, 120, 10)
c3 = Car('G wagon', 6, 150, 100)

c1.speedUp()
c1.slowDown()

c1.changeGear(4)

#print(c1.manu)
#print(c2.current_speed)
#print(c1.current_gear)
#print(c1.wheels)

