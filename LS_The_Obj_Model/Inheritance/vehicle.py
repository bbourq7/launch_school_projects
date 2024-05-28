class Vehicle:

    def stop(self):
        print('I am stopped')


class Car(Vehicle):

    def drive(self):
        print('I am driving.')

    def brake(self):
        super().stop()

class Truck(Vehicle):

    def drive(self):
        print('I am driving')

    def brake(self):
        super().stop()
