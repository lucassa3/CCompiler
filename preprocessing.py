class PreProcessing():

	def __init__(self):
		self.program_string = "0"

	def preprocess(self):
		return self.__remove_spaces()

	def __remove_spaces(self):
		return self.program_string.replace(" ", "")