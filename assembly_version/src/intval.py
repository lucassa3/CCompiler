from node import Node
from assembly import Assembly

class IntVal(Node):
    def eval(self, st):
        Assembly.write_program([f"MOV EBX, {self.value}"])
        return self.value