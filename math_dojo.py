class MathDojo(object):
	def __init__(self):
		self.sum = 0

	def __repr__(self):
		return "<MathDojo object sum {}>".format(self.sum)

	def add(self, *nums):
		for x in nums:
			if type(x) == int:
				self.sum += x
			else: 
				self.sum += sum(x)
		return self

	def subtract(self, *nums):
		for x in nums:
			if type(x) == int:
				self.sum -= x
			else: 
				self.sum -= sum(x)
		return self

	def result(self):
		return self.sum


if __name__ == "__main__":
	md = MathDojo()

	print md.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
