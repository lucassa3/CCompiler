from parser_temp import Parser

def main():
	input_data = "/*asl;dkas;dlk   lkl*/  +2) /**/"

	Parser.tokens.origin = input_data
	result = Parser.parse_expression()
	print(result)

if __name__ == "__main__":
	main()