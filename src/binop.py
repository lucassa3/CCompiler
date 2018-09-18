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
		


