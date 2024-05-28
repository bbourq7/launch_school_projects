class SignalMixin:

    def signal_left(self):
        print('Signalling Left')

    def signal_right(self):
        print('Signalling Right')

    def signal_off(self):
        print('Signalling OFF')


class Vehicle:
    all_vehicle_count = 0

    def __init__(self):
        Vehicle.all_vehicle_count += 1

    @classmethod
    def all_vehicles(self):
        print(Vehicle.all_vehicle_count)


class Car(SignalMixin, Vehicle):
    vehicles = 0
    
    def __init__(self):
        Car.vehicles += 1
        super().__init__()

    def vehicle(self):
        print(Car.vehicles)

class Truck(SignalMixin, Vehicle):
    vehicles = 0

    def __init__(self):
        Truck.vehicles += 1
        super().__init__()

    def vehicle(self):
        print(Truck.vehicles)


class Boat(Vehicle):
    vehicles = 0

    def __init__(self):
        Boat.vehicles += 1
        super().__init__()

    def vehicle(self):
        print(Truck.vehicles)