#multilevel inheritance
class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		Grandfather.__init__(self, grandfathername)

class daughter(Father):
	def __init__(self, daughtername, fathername, grandfathername):
		self.daughtername = daughtername

		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("daughter name :", self.daughtername)

s1 = daughter('rohini', 'vishnu', 'shiva')
s1.print_name()
 