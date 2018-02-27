class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		#self.display_all()

	def __repr__(self):
		return "<Car object price {}>".format(self.price)

	def display_all(self):
		print "Price: {}".format(self.price)
		print "Speed: {}".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Mileage: {}".format(self.mileage)
		print "Tax: {}".format(self.tax)

		return self

if __name__ == "__main__":
	car1 = Car(2000, "35mph", "Full", "15mpg")
	print " "
	car2 = Car(2000, "5mph", "Not Full", "105mpg")
	print " "
	car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
	print " "
	car4 = Car(2000, "25mph", "Full", "25mpg")
	print " "
	car5 = Car(2000, "45mph", "Empty", "25mpg")
	print " "
	car6 = Car(20000000, "25mph", "Empty", "15mpg")