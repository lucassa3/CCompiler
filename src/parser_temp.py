from tokenizer import Tokenizer

OPERATORS = ["MULT", "DIV", "PLUS", "MINUS"]

class Parser():
	
	tokens = Tokenizer()

	def parse_expression():
		result = 0
		Parser.tokens.next()
		
		result = Parser.parse_term()

		while Parser.tokens.current != None and (Parser.tokens.current.type == "PLUS" or Parser.tokens.current.type == "MINUS"):
			if Parser.tokens.current.type == "PLUS":
				Parser.tokens.next()

				term_result = Parser.parse_term()
				result += term_result
			

			elif Parser.tokens.current.type == "MINUS":
				Parser.tokens.next()

				term_result = Parser.parse_term()
				result -= term_result
			
			else:
				raise ValueError(f"Expecting an operator. Got: {Parser.tokens.current.type}")

		return result

	def parse_term():
		result = 0
		
		if Parser.tokens.current.type == "NUMBER":
			result += Parser.tokens.current.value
			Parser.tokens.next()

		else:
			raise ValueError(f"Expecting NUMBER. Got: {Parser.tokens.current.type}")

		while Parser.tokens.current != None and (Parser.tokens.current.type == "MULT" or Parser.tokens.current.type == "DIV"):
			if Parser.tokens.current.type == "MULT":
				Parser.tokens.next()

				if Parser.tokens.current.type == "NUMBER":
					result *= Parser.tokens.current.value
					Parser.tokens.next()

				else:
					raise ValueError(f"Expecting Number. Got: {Parser.tokens.current.type}")
			

			elif Parser.tokens.current.type == "DIV":
				Parser.tokens.next()

				if Parser.tokens.current.type == "NUMBER":
					result //= Parser.tokens.current.value
					Parser.tokens.next()

				else:
					raise ValueError(f"Expecting Number. Got: {Parser.tokens.current.type}")
			
			else:
				raise ValueError(f"Expecting an operator. Got: {Parser.tokens.current.type}")

		return result