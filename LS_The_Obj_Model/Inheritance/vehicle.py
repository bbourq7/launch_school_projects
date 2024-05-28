class Vehicle:

    def __init__(self, wheels):
        self.wheels = wheels
        print(f'I have {self.wheels} wheels.')

    def stop(self):
        print('I am stopped')

    def drive(self):
        print('I am driving')


class Car(Vehicle):

    def __init__(self):
        print('Creating a car')
        super().__init__(4)

    def drive(self):
        print('I am driving.')

    def brake(self):
        super().stop()

class Truck(Vehicle):

    def __init__(self):
        print('Creating a Truck')
        super().__init__(18)

    def drive(self):
        print('I am driving')

    def brake(self):
        super().stop()

class Motorcycle(Vehicle):

    def __init__(self):
        print('Creating a motorcycle.')
        super().__init__(2)

    def drive(self):
        super().drive()
        print('   No! I am riding')

