class Animal:

	@classmethod
	def make_sound(cls):
		print (f'{cls.__name__}: A generic sound')

class Dog(Animal):
	
	@classmethod
	def make_sound(cls):
		super().make_sound()
		print(f'{cls.__name__}: Bark')


