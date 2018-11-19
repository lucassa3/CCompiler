from node import Node
from assembly import Assembly

class LoopNode(Node):
    def eval(self, st):
        ass_mode = True
        if ass_mode:
            Assembly.write_program([f"LOOP_{self.identifier}:"])
            self.children[0].eval(st)
            Assembly.write_program([f"CMP EBX, False"])
            Assembly.write_program([f"JE EXIT_{self.identifier}"])
            self.children[1].eval(st)
            Assembly.write_program([f"JMP LOOP_{self.identifier}"])
            Assembly.write_program([f"EXIT_{self.identifier}:"])

        else:
            while self.children[0].eval(st) == True:
                self.children[1].eval(st)