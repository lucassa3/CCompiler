from node import Node

class UnOp(Node):
	def eval(self):
		a = self.children[0].eval()

		if self.value == "MINUS":
			return -a
		elif self.value == "PLUS":
			return +a