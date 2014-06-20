import math

class Point3d:
	def __init__(self, v=None):
		self.__v = Vector(4)
		self.__v[3] = 1.0
		for i in range(0, 3):
			self.__v[i] = v[i]
	def __getitem__(self, i):
		return self.__v[i] / self.__v[3]
	def __setitem__(self, i, val):
		self.__v[i] = self.__v[i] * self.__v[3]
	def __sub__(self, p2):
		return Vector3d([self[0] - p2[0], self[1] - p2[1], self[2] - p2[2]])
	def to3dVector(self):
		result = Vector3d()
		result[0] = self[0]
		result[1] = self[1]
		result[2] = self[2]
		return result
	def to4dVector(self):
		pass
	def to1x3Matrix(self):
		pass
	def to3x1Matrix(self):
		pass
	def to1x4Matrix(self):
		pass
	def to4x1Matrix(self):
		pass
	def __repr__(self):
		result = "x=%f, y=%f, z=%f"%(self[0], self[1], self[2])
		return result
			


class Vector:
	def __init__(self, dim, v=None):
		self.__v = []
		if v == None:
			for i in range(0, dim):
				self.__v.append(0)
		else:
			if dim == len(v):
				for e in v:
					self.__v.append(e)
			else:
				pass # Mettere Eccezione
	# Get Item
	def __getitem__(self, i):
		return self.__v[i]
	# Set Item
	def __setitem__(self, i, v):
		self.__v[i] = v	
	# Length
	def __len__(self):
		return len(self.__v)
	# Addition
	def __add__(self, b):	
		result = None
		if len(self) == len(b):
			result = Vector(len(self))
			for i in range(0, len(self)):
				result[i] = self[i] + b[i]
		
		return result
	
	# Subtraction
	def __sub__(self, b):	
		result = None
		if len(self) == len(b):
			result = Vector(len(self))
			for i in range(0, self.len()):
				result[i] = self[i] - b[i]
		
		return result
	# Dot product
	def __mul__(self, b):
		result = None
		if len(self) == len(b):
			result = 0
			for i in range(0, len(self)):
				result = result + self[i] * b[i]
		return result
	# Vector div Scalar
	def __div__(self, b):
		result = Vector(len(self))
		for i in range(0, len(self)):
			result[i] = self[i] / float( b )
		
		return result
	# Product scalar per Vector
	def scalarPerVector(self, s):
		result = Vector(len(self))
		for i in range(0, len(self)):
			result[i] = result[i] * s
	def clone(self):
		result = Vector(len(self), self)
		return result
			
	def __repr__(self):
		return self.__v.__repr__()
	def __normalize__(self):
		val = math.sqrt(self*self)
		result = self / val
		return result
	
class Vector3d(Vector):
	def __init__(self, v=None):
		Vector.__init__(self, 3, v)
	def __pow__(self, v):
		result = None
		if len(v) == 3:
			result = Vector3d()
			result[0] = self[1] * v[2] - self[2] * v[1]
			result[1] = self[2] * v[0] - self[0] * v[2]
			result[2] = self[0] * v[1] - self[1] * v[0]
		return result
	def clone(self):
		result = Vector3d(self)
		return result
	
""" Test 1
v1 = Vector(3, [1,2,3])
v2 = Vector(3, [4,5,6])

v3 = v1 + v2
v4 = v1 * v2
v5 = v1 / 3

x = Vector3d([1, 0, 0])
y = Vector3d([0, 1, 0])
z = x ** y

print(z)"""

p1 = Point3d([0, 0, 0])
print p1
p2 = Point3d([1, 0, 0])
print p2
p3 = Point3d([0, 1, 0])
print p3

v1 = p2 - p1
print v1
v2 = p3 - p1
print v2
v3 = v1**v2
print v3
p4 = Point3d(v3)

print p4




		