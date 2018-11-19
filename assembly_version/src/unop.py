from node import Node

class UnOp(Node):
	def eval(self, st):
		a = self.children[0].eval(st)

		if self.value == "MINUS":
			return -a
		elif self.value == "PLUS":
			return +a
		elif self.value == "NOT":
			return not a