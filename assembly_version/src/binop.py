from node import Node
from assembly import Assembly

class BinOp(Node):
	def eval(self, st):
		a = self.children[0].eval(st)
		Assembly.write_program(["PUSH EBX"])

		b = self.children[1].eval(st)
		Assembly.write_program(["POP EAX"])

		if self.value == "MINUS":
			Assembly.write_program(["SUB EAX, EBX"])
			Assembly.write_program(["MOV EBX, EAX"])
			return a - b
		elif self.value == "PLUS":
			Assembly.write_program(["ADD EAX, EBX"])
			Assembly.write_program(["MOV EBX, EAX"])
			return a + b
		elif self.value == "MULT":
			Assembly.write_program(["IMUL EBX"])
			Assembly.write_program(["MOV EBX, EAX"])
			return a * b
		elif self.value == "DIV":
			Assembly.write_program(["MOV EDX, 0"])
			Assembly.write_program(["IDIV EBX"])
			Assembly.write_program(["MOV EBX, EAX"])
			return a // b
		elif self.value == "GREATER":
			Assembly.write_program(["CMP EAX, EBX"])
			Assembly.write_program(["Call binop_jg"])
			return a > b
		elif self.value == "LESS":
			Assembly.write_program(["CMP EAX, EBX"])
			Assembly.write_program(["Call binop_jl"])
			return a < b
		elif self.value == "EQUALS":
			Assembly.write_program(["CMP EAX, EBX"])
			Assembly.write_program(["Call binop_je"])
			return a == b
		elif self.value == "AND":
			Assembly.write_program(["AND EAX, EBX"])
			Assembly.write_program(["MOV EBX, EAX"])
			return a and b
		elif self.value == "OR":
			Assembly.write_program(["OR EAX, EBX"])
			Assembly.write_program(["MOV EBX, EAX"])
			return a or b

		


