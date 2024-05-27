class GoodDog:
	
	def __init__(self, name):
		self.name = name
		print(f'Constructor for {self.name}')

	def speak(self):
		print(f'{self.name} says Woof!')

	def roll_over(self):
		print(f'{self.name} is rolling over.')


