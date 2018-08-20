from tokenizer import Tokenizer

class Parser():
	
	tokens = Tokenizer()

	def parse_expression():
		result = 0
		Parser.tokens.next()
		
		if Parser.tokens.current.type == "NUMBER":
			result += Parser.tokens.current.value
			Parser.tokens.next()

		else:
			raise ValueError(f"Expecting NUMBER. Got: {Parser.tokens.current.type}")

		while Parser.tokens.current != None and (Parser.tokens.current.type == "PLUS" or Parser.tokens.current.type == "MINUS"):
			if Parser.tokens.current.type == "PLUS":
				Parser.tokens.next()

				if Parser.tokens.current.type == "NUMBER":
					result += Parser.tokens.current.value
					Parser.tokens.next()

				else:
					raise ValueError(f"Expecting Number. Got: {Parser.tokens.current.type}")
			

			elif Parser.tokens.current.type == "MINUS":
				Parser.tokens.next()

				if Parser.tokens.current.type == "NUMBER":
					result -= Parser.tokens.current.value
					Parser.tokens.next()

				else:
					raise ValueError(f"Expecting Number. Got: {Parser.tokens.current.type}")
			
			else:
				raise ValueError(f"Expecting an operator. Got: {Parser.tokens.current.type}")

		return result