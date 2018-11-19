from node import Node
from assembly import Assembly

class PrintNode(Node):
	def eval(self, st):
		ass_mode = True
		if not ass_mode:
			print(self.children[0].eval(st))
		else:
			self.children[0].eval(st)
		Assembly.write_program(["PUSH EBX"])
		Assembly.write_program(["CALL print"])