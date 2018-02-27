from datetime import datetime
id_counter = 1

class Call(object):
	def __init__(self, caller_name, caller_phone, reason_for_call):
		global id_counter
		self.call_id = id_counter
		id_counter += 1
		self.caller_name = caller_name
		self.caller_phone = caller_phone
		self.time_of_call = datetime.now()
		self.reason_for_call = reason_for_call

	def __repr__(self):
		return "<Call object {}>".format(self.call_id)

	def display(self):
		print "Call ID: {}".format(self.call_id)
		print "Caller Name: {}".format(self.caller_name)
		print "Caller Phone: {}".format(self.caller_phone)
		print "Time of Call: {}".format(self.time_of_call)
		print "Reason for Call: {}".format(self.reason_for_call)
		return self


class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(self.calls)

	def __repr__(self):
		return "<CallCenter object queue size {}>".format(self.queue_size)

	def add(self, call):
		self.calls.append(call)
		self.queue_size = len(self.calls)
		return self

	def remove(self, call):
		self.calls.pop(0)
		self.queue_size = len(self.calls)
		return self

	# Ninja Level method. Removed a call based on phone number
	def remove_by_number(self, number):
		for call in self.calls:
			if call.caller_phone == number:
				self.calls.pop(self.calls.index(call))
				self.queue_size -= 1
		return self

	#hacker level method. Sort the calls by time
	def sort_by_time(self):
		self.calls = sorted(self.calls, key=lambda call: call.time_of_call)
		return self
	
	def info(self):
		for call in self.calls:
			print "Caller Name: {}, Caller Phone: {}".format(call.caller_name, call.caller_phone)

		print self.queue_size
		return self

if __name__ == "__main__":
	call1 = Call("Daniel", "1234567890", "Dog ate computer")
	call2 = Call("Nicole", "7894561230", "Computer is on fire")
	call3 = Call("Ivy", "1234567890", "I don't know how to use a computer. I'm 4.")
	call4 = Call("Hayden", "4567891234", "I lost my computer")
	#call1.display()

	callCenter1 = CallCenter().add(call4).add(call2).add(call1).add(call3).info()

	callCenter1.sort_by_time().info()
