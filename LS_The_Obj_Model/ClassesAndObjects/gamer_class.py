class Person:
	
	def __init__(self, name):
		self.name = name
		type_name = self.__class__.__name__
		print(f'I am {name}, a {type_name}.')

	def eat(self):
		print(f"{self.name}: Yummy!")
		

class Gamer(Person):

	def game(self):
		print(f"{self.name}: Let's Go!!!!")

	
