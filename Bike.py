class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def __repr__(self):
		return "<Bike object price {}, max speed {},  miles {}>".format(self.price, self.max_speed, self.miles)

	def displayInfo(self):
		print "Price: {}".format(self.price)
		print "Max Speed: {}".format(self.max_speed)
		print "Miles: {}".format(self.miles)
		return self

	def ride(self):
		self.miles += 10
		return self

	def reverse(self):
		self.miles -= 5
		# if the miles go negative, set it to zero. Can't have negative miles.
		if self.miles < 0:
			self.miles = 0
		return self

if __name__ == "__main__":
	bike1 = Bike(100, "15mph")
	bike2 = Bike(150, "20mph")
	bike3 = Bike(1, "50mph")


	bike1.ride().ride().ride().reverse().displayInfo()
	print " "
	bike2.ride().ride().reverse().reverse().displayInfo()
	print " "
	bike3.reverse().reverse().displayInfo()



	# All the methods except for the __init__ can return self to chain.