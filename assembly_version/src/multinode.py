from node import Node

class MultiNode(Node):
    '''created to handle multiple evals on the same level sequentially'''
    def eval(self, st):
        if self.children:
            for child in self.children:
                child.eval(st)