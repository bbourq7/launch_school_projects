class Performance:

    def __init__(self, fuel_capacity, mpg):
        self.fuel_capacity = fuel_capacity
        self.mpg = mpg

    def max_range(self):
        return self.fuel_capacity * self.mpg
    
class Car(Performance):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def max_range_in_miles(self):
        super().max_range(self.fuel_capacity, self.mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Performance):

    def __init__(self, fuel_capacity, mpg):
       super().__init__(fuel_capacity, mpg) 

    def max_range_in_miles(self):
        super().max_range(self.fuel_capacity, self.mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')
        