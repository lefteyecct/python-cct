pi = 3.14
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius        
    def volume(self):
        height = self.height
        radius = self.radius
        return height*pi*radius**2  
    def surface_area(self):
        height = self.height
        radius = self.radius
        power_radius = pow(radius,2)

        return 2*(pi* power_radius) + (2*pi*radius*height)


    # EXAMPLE OUTPUT
c = Cylinder(2,3)

print(c.volume()) # 56.52

print(c.surface_area()) # 94.2