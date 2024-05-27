class Car:

    def __init__(self, car, year, color):
        self.car_id = car
        self.year = year
        self.color = color
        
    def __str__(self):
        color = self.color.title()
        return f'{color} {self.year} {self.car_id}'
    
    def __repr__(self):
        color = repr(self.color)
        year = repr(self.year)
        model = repr(self.car_id)
        return f'Car({model}, {year}, {color})'
    
