from node import Node


class FuncCallNode(Node):
    def eval(self, st):
        func = st.get_var(self.value)
        if len(func.vardec) == len(self.children):
            if self.children:
                for arg, child in zip(func.vardec, self.children):
                    func.children[0].local_st.create_var(arg[1], arg[0])
                    func.children[0].local_st.set_var(arg[1], child.eval(st))
        else:
            raise ValueError(f"argument number passed doesnt matched! Received {len(self.children)} args but function needs {len(func.vardec)}!")

        if func.vartype != "void":
            func.children[0].local_st.create_var("return", func.vartype)

        func.children[0].eval(st)

        if func.vartype != "void":
            return func.children[0].local_st.get_var("return")