class Foo1:
	
	@classmethod
	def bar(cls):
		print('this is bar in Foo1')

	def qux(self):
		type(self).bar()
		self.__class__.bar()
		self.bar()
		Foo1.bar()

class Foo2(Foo1):

	@classmethod
	def bar(cls):
		print('this is bar in Foo2')


