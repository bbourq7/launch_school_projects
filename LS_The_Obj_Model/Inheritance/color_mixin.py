class ColorMixin:

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
    
class Car(ColorMixin):

    def __init__(self, color):
        self.set_color(color)

class SmartLight(ColorMixin):

    def __init__(self, color):
        self.set_color(color)

class House(ColorMixin):
    
    def __init__(self, color):
        self.set_color(color)