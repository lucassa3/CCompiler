from uuidmanager import UUIDManager

class Node():
	def __init__(self, value=None):
		self.value = value
		self.children = []
		self.identifier = UUIDManager.get_new()

	def set_child(self, child):
		self.children.append(child)