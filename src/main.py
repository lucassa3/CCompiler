import sys
from parser_temp import Parser

def main():
    with open(sys.argv[1], 'r') as myfile:
        input_data=myfile.read().replace('\n', '')

    Parser.tokens.origin = input_data
    result = Parser.parse_expression()
    print(result.eval())

if __name__ == "__main__":
    main()