from node import Node

class ReturnNode(Node):
    def eval(self, st):
        st.set_var("return", self.children[0].eval(st))
