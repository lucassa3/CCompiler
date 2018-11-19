from node import Node
from assembly import Assembly


class VarDecNode(Node):
    def __init__(self, value, vartype):
        super(self.__class__, self).__init__(value)
        self.vartype = vartype

    def eval(self, st):
        Assembly.write_bss(f"{self.value}_{st.identifier} RESD 1")
        st.create_var(self.value, self.vartype)