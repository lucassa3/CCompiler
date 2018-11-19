from node import Node
from assembly import Assembly


class CondNode(Node):
    def eval(self, st):
        ass_mode = True
        if not ass_mode:
            if self.children[0].eval(st) == True:
                self.children[1].eval(st)

            else:
                if len(self.children) > 2:
                    self.children[2].eval(st)
        else:
            if len(self.children) > 2:
                self.children[0].eval(st)
                Assembly.write_program([f"CMP EBX, False"])
                Assembly.write_program([f"JE ELSE_{self.identifier}"])
                self.children[1].eval(st)
                Assembly.write_program([f"JMP EXIT_{self.identifier}"])
                Assembly.write_program([f"ELSE_{self.identifier}:"])
                self.children[2].eval(st)
                Assembly.write_program([f"EXIT_{self.identifier}:"])
            else:
                self.children[0].eval(st)
                Assembly.write_program([f"CMP EBX, False"])
                Assembly.write_program([f"JE EXIT_{self.identifier}"])
                self.children[1].eval(st)
                Assembly.write_program([f"EXIT_{self.identifier}:"])

