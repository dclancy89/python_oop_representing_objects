class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def __repr__(self):
		return "<Animal object {}, health {}>".format(self.name, self.health)

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Health: {}".format(self.health)
		return self



class Dog(Animal):
	def __init__(self):
		super(Dog, self).__init__("dog", 150)

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self):
		super(Dragon, self).__init__("dragon", 170)

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		super(Dragon, self).displayHealth()
		print "I am a Dragon"
		return self

if __name__ == "__main__":
	animal1 = Animal("Generic Animal", 100).walk().walk().walk().run().run().displayHealth()

	dog1 = Dog().walk().walk().walk().run().run().pet().displayHealth()  #.fly() Doesn't work!

	dragon1 = Dragon().fly().displayHealth()

	#animal2 = Animal("Badger", 80).pet() # doesn't work!

	#animal2 = Animal("Badger", 80).fly() # doesn't work!