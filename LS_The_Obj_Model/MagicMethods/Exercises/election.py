import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        self.x -= other.x
        self.y -= other.y
        return Vector(self.x, self.y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        dot_product = ((self.x * other.x)+(self.y * other.y))
        return dot_product
    
    def __abs__(self):
        sum_of_squares = ((self.x ** 2) + (self.y **2))
        return math.sqrt(sum_of_squares)