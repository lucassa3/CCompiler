import sys
from parser_temp import Parser
from symboltable import SymbolTable

def main():
    with open(sys.argv[1], 'r') as myfile:
        input_data=myfile.read().replace('\n', '')

    st = SymbolTable()
    Parser.tokens.origin = input_data
    result = Parser.init_parse()
    result.eval(st)

if __name__ == "__main__":
    main()