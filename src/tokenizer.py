from string import ascii_letters, digits
from token import Token

SINGLE_CHAR = {
	"+": "PLUS",
	"-": "MINUS",
	"*": "MULT",
	"/": "DIV"
}

class Tokenizer():

	def __init__(self):
		self.origin = "0"
		self.position = 0
		self.current = None

	def _isnumber(self, token):
		return token.isdigit()

	def _isalpha(self, token):
		return token.isalpha()

	def _isdirty(self):
		is_dirty = True
		while is_dirty:
			if self.position < len(self.origin):

				if self.origin[self.position] == " ":
					self.position += 1

				elif self.origin[self.position] == "\n":
					self.position+=1
					self.line_number += 1
				
				else:
					is_dirty = False
			else:
				is_dirty = False

	def next(self):
		aux = ""

		self._isdirty()

		if self.position < len(self.origin):

			if self._isnumber(self.origin[self.position]):
				while self._isnumber(self.origin[self.position]):

					aux += self.origin[self.position]

					self.position += 1

					if self.position > len(self.origin)-1:
						break

				self.current = Token("NUMBER", int(aux))
				aux = ""

			elif self.origin[self.position] in SINGLE_CHAR:
				self.current = Token(SINGLE_CHAR[self.origin[self.position]])
				self.position += 1

			else:
				raise ValueError(f"invalid token {self.origin[self.position]}")
		else:
			self.current = None