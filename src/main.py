from parser_temp import Parser

def main():
	input_data = "/* bla   */ 4*3+3    /* bla   */"

	Parser.tokens.origin = input_data
	result = Parser.parse_expression()
	print(result)

if __name__ == "__main__":
	main()