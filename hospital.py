# set a global counter for setting a unique patient ID
id_counter = 1

class Patient(object):
	def __init__(self, name, allergies):
		global id_counter
		self.id = id_counter
		id_counter += 1
		self.name = name
		self.allergies = allergies
		self.bed_number = None

	def __repr__(self):
		return "<Patient object id {}>".format(self.id)

	def info(self):
		print "Patient ID: {}".format(self.id)
		print "Patient Name: {}".format(self.name)
		print "Allergies: {}".format(self.allergies)
		print "Bed Number: {}".format(self.bed_number)
		print " "
		return self


class Hospital(object):
	def __init__(self, name, capacity):
		self.beds = [] 								# a list of all the available beds in the hospital
		for x in range(1, capacity + 1):
			self.beds.append(x)
		self.patients = []
		self.name = name
		self.capacity = capacity

	def __repr__(self):
		return "<Hospital Object name {}>".format(self.name)

	def admit(self, patient):
		if len(self.patients) < self.capacity:
			self.patients.append(patient)  			# add patient to patients list
			patient.bed_number = self.beds[0]		# assign them the first open bed
			self.beds.pop(0)						# remove that bed from the list
		else:
			print "Cannot admit {} because we have no open beds.".format(patient.name)
		return self

	def discharge(self, patient):
		self.patients.remove(patient)				# remove the patient from the patients list
		self.beds.append(patient.bed_number)		# add their bed number to the open beds
		patient.bed_number = None 					# set the patient bed number to None

	def show_beds(self):
		print self.beds
		return self


if __name__ == "__main__":

	patient1 = Patient("Daniel", ['none'])
	patient2 = Patient("Nicole", ['cats', 'Justin'])

	hospital1 = Hospital("Richton Park", 1)
	hospital1.admit(patient1).admit(patient2)
	patient1.info()
	patient2.info()
	hospital1.discharge(patient1)

	hospital1.show_beds()



