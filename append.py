import math
class Box(object):
	G = 9.81
	def __init__(self, length, width, height):
		self.length = length
		self.width = width
		self.height = height

	def calculate_BCT(self, safety_factor, layers):
		#W*g*sf*l
		self.safety_factor = safety_factor
		self.layers = layers
		self.bct = self.G*self.length*self.width*self.height*self.safety_factor*self.layers/100000000000
		return self.bct

	def calculate_ECT(self):
		self.ect = self.calculate_BCT(5,9)*math.sqrt(2*(self.length+self.width))
		return self.ect

b1 = Box(420,250,300)

print(b1.calculate_BCT())
print(b1.calculate_ECT())