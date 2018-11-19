from node import Node


class VarDecNode(Node):
    def __init__(self, value, vartype):
        super(self.__class__, self).__init__(value)
        self.vartype = vartype

    def eval(self, st):
    	st.create_var(self.value, self.vartype)

        