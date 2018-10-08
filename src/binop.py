from node import Node

class BinOp(Node):
	def eval(self, st):
		a = self.children[0].eval(st)
		b = self.children[1].eval(st)

		if self.value == "MINUS":
			return a - b
		elif self.value == "PLUS":
			return a + b
		elif self.value == "MULT":
			return a * b
		elif self.value == "DIV":
			return a // b
		elif self.value == "GREATER":
			return a > b
		elif self.value == "LESS":
			return a < b
		elif self.value == "GE":
			return a >= b
		elif self.value == "LE":
			return a <= b
		elif self.value == "EQUALS":
			return a == b
		elif self.value == "AND":
			return a and b
		elif self.value == "OR":
			return a or b

		


