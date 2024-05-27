class Car:
	
	def __init__(self, model, year, color):
		self._model = model
		self._year = year
		self._color = color
		self.speed = 0
		self.acceleration = 0
		self.brake_power = 1
		self.state = 'Off'
		print(f'Thanks for entering your {color} {year} {model} in to the class object!')
		print(f'You are going {self.speed} MPH')

	def is_on_off(self):
		print (f'Your vehicle is {self.state}')
	
	def start(self):
		self.state = 'On'
		print (f'Vroooom!!')
		self.is_on_off()

	def accelerate(self):
		if self.state == 'Off':
			print(f"Your car is {self.state}, you can't accelerate..")
		else:
			self.acceleration += 1
			self.speed += self.acceleration
			print(f'Your current acceleration is: {self.acceleration}')
			print(f'Your current speed is {self.speed}')

	def brake(self):
		if self.speed == 0:
			print(f'Your speed is {self.speed}. Braking did nothing..')
		if self.acceleration >= 1:
			self.acceleration = 0
			print(f'Your acceleration is now {self.acceleration}')
		if self.speed > 0:
			self.speed -= self.brake_power
			if self.speed < 0:
				self.speed = 0
			print(f'Your current speed is {self.speed}')
		
	def check_speed(self):
		print(f'Your current speed is {self.speed} MPH.')

	def stop(self):
		if self.state == 'Off':
			print(f"Your car is already {self.state}, you can't turn it off again..")
		else:
			self.state = 'Off'
			print(f'<crickets>')
			self.is_on_off()
			self.speed = 0

	def spray_paint_car(self, color):
		self.color = color
		print(f'New paint job! Looking niiiicce! Your car is now {color}')

	@property
	def color(self):
		return self._color
	
	@color.setter
	def color(self, color):
		self._color = color

	@property
	def model(self):
		return self._model
	
	@property
	def year(self):
		return self._year
	
		
                
	
