from node import Node

class CondNode(Node):
    def eval(self, st):
        if self.children[0].eval(st) == True:
            self.children[1].eval(st)
        else:
            if len(self.children) > 2:
                self.children[2].eval(st)