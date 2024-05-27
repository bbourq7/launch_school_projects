class Car:
	
	def __init__(self, model, year, color):
		self.model = model
		self.year = year
		self.color = color
		self.speed = 0
		self.state = 'Off'
		print(f'Thanks for entering your {color} {year} {model} in to the class object!')
		print(f'You are going {self.speed} MPH')

	def is_on_off(self):
		print (f'Your vehicle is {self.state}')
	
	def start(self):
		self.state = 'On'
		print (f'Vroooom!!')
		self.is_on_off()
                
	
