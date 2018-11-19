from node import Node
from assembly import Assembly
class AssignerNode(Node):
	def eval(self, st):
		res = st.set_var(self.value, self.children[0].eval(st))
		Assembly.write_program([f"MOV [{self.value}_{res}], EBX"])