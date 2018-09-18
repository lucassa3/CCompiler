from tokenizer import Tokenizer
from binop import BinOp
from noop import NoOp
from unop import UnOp
from intval import IntVal
from assignernode import AssignerNode
from identifiernode import IdentifierNode
from printnode import PrintNode
from commandsnode import CommandsNode

class Parser():
    
    tokens = Tokenizer()

    def init_parse():
        Parser.tokens.next()
        result = Parser.parse_commands()
        Parser.tokens.next()

        if Parser.tokens.current != None:
            raise ValueError("oops something wr0ng happ3n3d")
        return result

    def parse_commands():
        if Parser.tokens.current.type == "OPEN_BLOCK":
            result = CommandsNode(Parser.tokens.current.type)
            result.set_child(Parser.parse_command())

            if Parser.tokens.current.type != "CMD_END":
                print(Parser.tokens.current.type)
                raise ValueError(f"Did not closed command")

            while Parser.tokens.current.type == "CMD_END":
                result.set_child(Parser.parse_command())


            if Parser.tokens.current.type != "CLOSE_BLOCK":
                 raise ValueError(f"Did not close block")

        else:
            raise ValueError(f"Did not open block")


        Parser.tokens.next()
        return result

    def parse_command():
        Parser.tokens.next()

        if Parser.tokens.current.type == "PRINT":
            return Parser.parse_print()

        if Parser.tokens.current.type == "IDENTIFIER":
            return Parser.parse_assignment()

        if Parser.tokens.current.type == "OPEN_BLOCK":
            return Parser.parse_commands()

        else:
            return NoOp()

    def parse_print():
        result = PrintNode()
        Parser.tokens.next()

        if Parser.tokens.current.type == "OPEN_PAR":
            result.set_child(Parser.parse_expression())

            if Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(f"Parse error")
                
        else:
            raise ValueError(f"Parse error")

        Parser.tokens.next()
        return result

    def parse_assignment():
        # print(Parser.tokens.current.value)
        result = AssignerNode(Parser.tokens.current.value)
        Parser.tokens.next()

        if Parser.tokens.current.type =="EQUAL":
            result.set_child(Parser.parse_expression())

        else:
            raise ValueError(f"Parse error")

        return result

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
       
        elif Parser.tokens.current.type == "IDENTIFIER":
            result = IdentifierNode(Parser.tokens.current.value)
            Parser.tokens.next()

        elif Parser.tokens.current.type == "MINUS":
            result = UnOp(Parser.tokens.current.type)
            Parser.tokens.next()
            result.set_child(Parser.parse_factor())

        elif Parser.tokens.current.type == "PLUS":
            result = UnOp(Parser.tokens.current.type)
            Parser.tokens.next()
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
            raise ValueError(f"Parse error")

        return result