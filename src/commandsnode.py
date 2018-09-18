from node import Node

class CommandsNode(Node):
    def eval(self, st):
        for child in self.children:
            child.eval(st)