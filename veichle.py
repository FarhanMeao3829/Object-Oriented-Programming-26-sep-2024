class Vehicle:
    
    def __init__(self, max_speed, milage):
        
        self.max_speed = max_speed
        self.milage = milage
        
tesla = Vehicle(120, 11)
lambo = Vehicle(280, 20)

print("Tesla max speed :", tesla.max_speed)
print("Tesla milage :", tesla.milage)

print("Lambo max speed :", lambo.max_speed )
print("Lambo milage :", lambo.milage )

if lambo.max_speed > tesla.max_speed:
    print("Lambo is faster than Tesla!")
    
else:
    print("Still lambo better cuz its a petrol based car")