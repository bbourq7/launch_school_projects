class Foo:
	def __init__(self, name):
		self.name = name
		type_name = self.__class__.__name__

	def fighter(self):
		type_name = self.__class__.__name__
		print(type_name)

