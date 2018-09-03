from tokenizer import Tokenizer
from binop import BinOp
from unop import UnOp
from intval import IntVal


OPERATORS = ["MULT", "DIV", "PLUS", "MINUS"]

class Parser():
	
	tokens = Tokenizer()

	def parse_expression():
		result = 0
		Parser.tokens.next()
		
		result = Parser.parse_term()

		while Parser.tokens.current != None and (Parser.tokens.current.type == "PLUS" or Parser.tokens.current.type == "MINUS"):
			result_cp = result
			result = BinOp(Parser.tokens.current.type)

			Parser.tokens.next()

			
			
			result.set_child(result_cp)
			result.set_child(Parser.parse_term())

		return result

	def parse_term():
		result = 0
		
		result = Parser.parse_factor()

		while Parser.tokens.current != None and (Parser.tokens.current.type == "MULT" or Parser.tokens.current.type == "DIV"):
			result_cp = result
			result = BinOp(Parser.tokens.current.type)
			Parser.tokens.next()

			
			
			result.set_child(result_cp)
			result.set_child(Parser.parse_factor())

		return result


	def parse_factor():
		result = 0

		if Parser.tokens.current.type == "NUMBER":

			result = IntVal(Parser.tokens.current.value)
			Parser.tokens.next()

		elif Parser.tokens.current.type == "MINUS":
			Parser.tokens.next()
			result = UnoOp(Parser.tokens.current.type)
			result.set_child(Parser.parse_factor())

		elif Parser.tokens.current.type == "PLUS":
			Parser.tokens.next()
			result = UnoOp(Parser.tokens.current.type)
			result.set_child(Parser.parse_factor())


		elif Parser.tokens.current.type == "OPEN_PAR":
			result = Parser.parse_expression()

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