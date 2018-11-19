class Node():

	def __init__(self, value=None):
		self.value = value
		self.children = []

	def set_child(self, child):
		self.children.append(child)