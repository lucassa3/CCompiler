from node import Node
from assembly import Assembly

class IdentifierNode(Node):
	def eval(self, st):
		res = st.get_var(self.value)
		Assembly.write_program([f"MOV EBX, [{self.value}_{res[1]}]"])
		return res[0]