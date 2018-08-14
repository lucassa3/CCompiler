from tokenizer import Tokenizer
from preprocessing import PreProcessing

class Parser():
	
	tokens = Tokenizer()

	def parse_expression():
		result = 0
		Parser.tokens.next()
		if Parser.tokens.current.type == "NUMBER":
			result += Parser.tokens.current.value
			Parser.tokens.next()

		while Parser.tokens.current != None and (Parser.tokens.current.type == "PLUS" or Parser.tokens.current.type == "MINUS"):
			if Parser.tokens.current.type == "PLUS":
				Parser.tokens.next()

				if Parser.tokens.current.type == "NUMBER":
					result += Parser.tokens.current.value
					Parser.tokens.next()

			elif Parser.tokens.current.type == "MINUS":
				Parser.tokens.next()

				if Parser.tokens.current.type == "NUMBER":
					result -= Parser.tokens.current.value
					Parser.tokens.next()

		return result

def main():
	input_data = "   10   +  20 +  30 +   100 -   60     +    321"
	preproc  = PreProcessing()
	preproc.program_string = input_data
	Parser.tokens.origin = preproc.preprocess()
	result = Parser.parse_expression()
	print(result)

if __name__ == "__main__":
	main()