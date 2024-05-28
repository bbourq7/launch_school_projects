from color_mixin import ColorMixin

class Car(ColorMixin):

    def __init__(self, color):
        self.set_color(color)

    #def set_color(self, color):
        #self._color = color

class SmartLight(ColorMixin):

    def __init__(self, color):
        self.set_color(color)

    #def set_color(self, color):
    #    self._color = color

    def get_color(self):
        return self._color
    
class House(ColorMixin):

    def __init__(self, color):
        self.set_color(color)

    #def set_color(self, color):
    #    self._color = color

    def get_color(self):
        return self.set_color
