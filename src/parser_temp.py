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



		if Parser.tokens.current == None or Parser.tokens.current.type == "CLOSE_PAR": #vai dar errado, mas wahtever
			return result
		else:
			raise ValueError(f"Could not complete the operation, please check your syntax")

	def parse_term():
		result = 0
		
		result = Parser.parse_factor()

		while Parser.tokens.current != None and (Parser.tokens.current.type == "MULT" or Parser.tokens.current.type == "DIV"):
			if Parser.tokens.current.type == "MULT":
				Parser.tokens.next()

				result *= Parser.parse_factor()
			

			elif Parser.tokens.current.type == "DIV":
				Parser.tokens.next()

				result //= Parser.parse_factor()
			
			else:
				raise ValueError(f"Expecting an operator. Got: {Parser.tokens.current.type}")

		return result


	def parse_factor():
		result = 0

		if Parser.tokens.current.type == "NUMBER":

			result += Parser.tokens.current.value
			Parser.tokens.next()

		elif Parser.tokens.current.type == "MINUS":
			Parser.tokens.next()
			result_factor = Parser.parse_factor()
			result -= result_factor

		elif Parser.tokens.current.type == "PLUS":
			Parser.tokens.next()
			result_factor = Parser.parse_factor()
			result += result_factor


		elif Parser.tokens.current.type == "OPEN_PAR":
			result_factor = Parser.parse_expression()
			result += result_factor

			if Parser.tokens.current != None:
				if Parser.tokens.current.type == "CLOSE_PAR":
					Parser.tokens.next()
				else:
					raise ValueError(f"Expecting Closing Parenthesis")

			else:	
				raise ValueError(f"Expecting Closing Parenthesis")


		else:
			raise ValueError(f"Expecting Number. Got: {Parser.tokens.current.type}")

		return result