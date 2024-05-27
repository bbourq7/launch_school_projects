class GoodDog:

	def __init__ (self, name, age):
		self.name = name
		self.age = age
		
	def speak(self):
		return f'{self._name} says arf!'

	def set_name(self, new name):
		if not isintance(new_name, str):
			raise TypeError('Name must be a string')
		self._name = new_name

	def age(self):
		return self._age

	def set_age(self, new_age):
		if not isinstance(new_age, int):
			raise TypeError('Age nust be an integer')
		if new_age < 0:
			raise ValueError("Age can't be negative")
		self._age = new_age


