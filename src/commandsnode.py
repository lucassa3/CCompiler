from node import Node
from symboltable import SymbolTable

class CommandsNode(Node):
    def __init__(self, value, local_st):
        super(self.__class__, self).__init__(value)
        self.local_st = local_st
    
    def eval(self, st):
        self.local_st.father = st

        for child in self.children:
            child.eval(self.local_st)