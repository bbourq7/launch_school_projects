class Pet:
	
	def __init__(self, name):
		self.name = name
		type_name = type(self).__name__
		print(f'I am {name}, a {type_name}.')

class Dog(Pet):
	
	def speak(self):
		print(f'{self.name} says Woof!')

	def roll_over(self):
		print(f'{self.name} is rolling over.')

class Cat(Pet):
	
	def speak(self):
		print(f'{self.name} says Meow!')

	def cough(self):
		print('Hair Ball!?!')

class Parrot(Pet):

	def speak(self):
		print(f'{self.name} wants a cracker!')

	def flap(self):
		print(f'{self.name} flys away!!!')


