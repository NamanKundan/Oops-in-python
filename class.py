class circle:
    pi = 3.14
    def __init__(self,radius=6,):
        self.radius = radius
        self.area = circle.pi*radius*radius
    def circumference(self):
        return 2*circle.pi*self.radius
    
circle1 = circle(4)
print(circle1.circumference())
print(circle1.area)
