class GoodCat:

	counter = 0

	def __init__(self, name, age):
		GoodCat.counter += 1

	@classmethod
	def number_of_cats(cls):
		return GoodCat.counter


