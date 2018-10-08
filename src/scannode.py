from node import Node

class ScanNode(Node):
    def eval(self, st):
        self.value = input("scan: ")
        return int(self.value)