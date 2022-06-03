from curses.textpad import rectangle
from math import radians

# circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        PI=3.142 * (self.radius)
        return PI
    def circumf(self):
        sum=2 * (3.12 * self.radius)
        return sum
    # Square    
class Square():
    def __init__(self,sides):
        self.sides=sides
    def square(self):
        perimeter=4 * (self.sidej)
        return perimeter
    # rect
class Rect():
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def areaR(self):
        perimeter=2 * (self.w + self.l)
        return perimeter
    # sphere

class Sphere():
    def ___init__(self,radiusone):
        self.radiusone=radiusone
    def surf_area(self):
        sphereArea= 4 * (3.142 * (self.radiusone))
        return sphereArea

    def volume(self):
        sphereV=4/3 * (3.142 * (self.radiusone * self.radiusone * self.radiusone))





