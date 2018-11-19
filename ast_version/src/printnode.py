from node import Node

class PrintNode(Node):
	def eval(self, st):
		print(self.children[0].eval(st))