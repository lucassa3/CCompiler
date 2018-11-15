from node import Node

class AssignerNode(Node):
	def eval(self, st):
		# print(self.value)
		# print(self.children[0].eval(st))
		st.set_var(self.value, self.children[0].eval(st))