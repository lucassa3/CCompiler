from node import Node


class FuncDecNode(Node):
    def __init__(self, value, vartype):
        super(self.__class__, self).__init__(value)
        self.vartype = vartype
        self.vardec = []
        self.self_reference = None

    def eval(self, st):
        st.create_var(self.value, "FUNCTION")
        st.set_var(self.value, self.self_reference)