from parser_temp import Parser

def main():
	input_data = "   /* oi */1111+2+3-2 /*  asdkasdl;k;lk */    /**/"

	Parser.tokens.origin = input_data
	result = Parser.parse_expression()
	print(result)

if __name__ == "__main__":
	main()