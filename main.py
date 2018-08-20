from parser_temp import Parser

def main():
	input_data = "   10   +  20 +  30 +   100 -   60     +    321"

	Parser.tokens.origin = input_data
	result = Parser.parse_expression()
	print(result)

if __name__ == "__main__":
	main()