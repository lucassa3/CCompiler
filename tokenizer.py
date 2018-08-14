from string import ascii_letters, digits
from token import Token

class Tokenizer():

	def __init__(self):
		self.origin = "0"
		self.position = 0
		self.current = None

	def _isnumber(self, token):
		return token.isdigit()

	def _isalpha(self, token):
		return token.isalpha()

	def next(self):
		aux = ""
		if self.position < len(self.origin)-1:

			if self._isnumber(self.origin[self.position]):
				while self._isnumber(self.origin[self.position]):

					aux += self.origin[self.position]

					self.position += 1

					if self.position > len(self.origin)-1:
						break

				self.current = Token("NUMBER", int(aux))
				aux = ""

			elif self.origin[self.position] == "+":
				self.current = Token("PLUS")
				self.position += 1

			elif self.origin[self.position] == "-":
				self.current = Token("MINUS")
				self.position += 1

			else:
				raise ValueError("nao identifiquei algum caracter durante o calculo :(")
		else:
			self.current = None




