
""" currencies module
add value of different currencies
"""

class Ccy:
	""" currencies class
	"""
	def __init__(self, value, unit):
		""" init 
		"""
		self.value = value
		self.unit = unit
		self.__ratio = dict(zip(["EURUSD", "USDEUR"], [1.17, 0.85]))
	
	def convert(self, value, unit):
		""" convert 'value' of currency to 'unit'
		"""
		return value * self.__ratio[unit]
			
	def __add__(self, other):
		""" add 
		"""
		if type(other) is int or type(other) is float:
			return str(self.value + other) + " " + self.unit
		else:
			return str(self.value + self.convert(other.value, other.unit+self.unit)) + " " + self.unit
	
	def __radd__(self, other):
		""" radd
		"""
		return self + other


v1 = Ccy(23.43, "EUR")
v2 = Ccy(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)
print(3 + v1)
