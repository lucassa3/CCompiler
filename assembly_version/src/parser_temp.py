from tokenizer import Tokenizer
from binop import BinOp
from noop import NoOp
from unop import UnOp
from intval import IntVal
from assignernode import AssignerNode
from identifiernode import IdentifierNode
from printnode import PrintNode
from commandsnode import CommandsNode
from condnode import CondNode
from loopnode import LoopNode
from scannode import ScanNode
from vardecnode import VarDecNode

class Parser():
    
    tokens = Tokenizer()

    def init_parse():
        Parser.tokens.next()
        result = Parser.parse_program()

        if Parser.tokens.current != None:
            raise ValueError("oops something wr0ng happ3n3d")
        return result

    def parse_program():
        result = 0
        if Parser.tokens.current.type == "INT" or Parser.tokens.current.type == "VOID":
            Parser.tokens.next()
            
            if Parser.tokens.current.type == "MAIN":
                Parser.tokens.next()
                
                if Parser.tokens.current.type == "OPEN_PAR":
                    Parser.tokens.next()
                    
                    if Parser.tokens.current.type == "CLOSE_PAR":
                        Parser.tokens.next()
                        
                        if Parser.tokens.current.type == "OPEN_BLOCK":
                            result = Parser.parse_commands()
                            Parser.tokens.next()
                        
                        else:
                            raise ValueError(f"Expecting opening block. Got: {Parser.tokens.current.type}")
                    else:
                        raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
                else:
                    raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting main. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting type void. Got: {Parser.tokens.current.type}")
        
        return result    


    def parse_commands():
        if Parser.tokens.current.type == "OPEN_BLOCK":
            result = CommandsNode(Parser.tokens.current.type)
            has_op = True
            Parser.tokens.next()
            while has_op:
                child = Parser.parse_command()
                result.set_child(child)
                if isinstance(child, NoOp):
                    has_op = False

            if Parser.tokens.current.type != "CLOSE_BLOCK":
                raise ValueError(f"Expecting closing block. Got: {Parser.tokens.current.type}")

        else:
            raise ValueError(f"Expecting closing block. Got: {Parser.tokens.current.type}")
        
        Parser.tokens.next()
        return result

    def parse_command():
        if Parser.tokens.current.type == "PRINT":
            return Parser.parse_print()
        
        if Parser.tokens.current.type == "INT" or \
           Parser.tokens.current.type == "CHAR":
            return Parser.parse_vardec()

        if Parser.tokens.current.type == "IDENTIFIER":
            return Parser.parse_assignment()

        if Parser.tokens.current.type == "OPEN_BLOCK":
            return Parser.parse_commands()

        if Parser.tokens.current.type == "IF":
            return Parser.parse_if_else()

        if Parser.tokens.current.type == "WHILE":
            return Parser.parse_while()

        else:
            return NoOp()

    def parse_vardec():
        result = 0
        var_type = Parser.tokens.current.type
        Parser.tokens.next()

        if Parser.tokens.current.type == "IDENTIFIER":
            result = VarDecNode(Parser.tokens.current.value, var_type)
        
        Parser.tokens.next()
        
        if Parser.tokens.current.type != "CMD_END":
            raise ValueError(f"Expecting CMD_END token. Got: {Parser.tokens.current.type}")
        
        Parser.tokens.next()
        return result
    

    def parse_if_else():
        result = CondNode()
        Parser.tokens.next()

        if Parser.tokens.current.type == "OPEN_PAR":
            result.set_child(Parser.parse_bool_expression())

            if Parser.tokens.current.type == "CLOSE_PAR":
                Parser.tokens.next()

                if Parser.tokens.current.type == "OPEN_BLOCK":
                    result.set_child(Parser.parse_commands())

                    if Parser.tokens.current.type == "ELSE":
                        Parser.tokens.next()
                        result.set_child(Parser.parse_commands())

                else:
                    raise ValueError(f"Expecting opening block. Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return result

    def parse_while():
        result = LoopNode()
        Parser.tokens.next()

        if Parser.tokens.current.type == "OPEN_PAR":
            result.set_child(Parser.parse_bool_expression())

            if Parser.tokens.current.type == "CLOSE_PAR":
                Parser.tokens.next()

                if Parser.tokens.current.type == "OPEN_BLOCK":
                    result.set_child(Parser.parse_commands())

                else:
                    raise ValueError(f"Expecting opening block. Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return result

    def parse_bool_expression():
        
        result = Parser.parse_bool_term()

        while Parser.tokens.current != None and Parser.tokens.current.type == "OR":
            result_cp = result
            result = BinOp(Parser.tokens.current.type)

            result.set_child(result_cp)
            result.set_child(Parser.parse_bool_term())

        return result

    def parse_bool_term():
        
        result = Parser.parse_bool_factor()

        while Parser.tokens.current != None and Parser.tokens.current.type == "AND":

            result_cp = result
            result = BinOp(Parser.tokens.current.type)

            result.set_child(result_cp)
            result.set_child(Parser.parse_bool_factor())

        return result


    def parse_bool_factor():
        result = 0
       
        if Parser.tokens.current.type == "NOT":
            result = UnOp(Parser.tokens.current.type)
            Parser.tokens.next()
            result.set_child(Parser.parse_bool_factor())


        else:
            result = Parser.parse_rel_expression()

        return result

    def parse_rel_expression():
        Parser.tokens.next()
        result = Parser.parse_expression()


        if Parser.tokens.current.type == "LESS" or Parser.tokens.current.type == "GREATER" \
        or Parser.tokens.current.type == "EQUALS" or Parser.tokens.current.type == "LE" or \
        Parser.tokens.current.type == "GE":
            result_cp = result
            result = BinOp(Parser.tokens.current.type)

            Parser.tokens.next()
            
            result.set_child(result_cp)
            result.set_child(Parser.parse_expression())

        return result


    def parse_print():
        result = PrintNode()
        Parser.tokens.next()

        if Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()
            result.set_child(Parser.parse_expression())

            if Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(f"Parse error")
                
        else:
            raise ValueError(f"Parse error")

        Parser.tokens.next()

        if Parser.tokens.current.type != "CMD_END":
            raise ValueError(f"Expecting CMD_END token. Got: {Parser.tokens.current.type}")

        Parser.tokens.next()
        return result



    def parse_assignment():
        result = AssignerNode(Parser.tokens.current.value)
        Parser.tokens.next()

        if Parser.tokens.current.type =="EQUAL":
            Parser.tokens.next()

            if Parser.tokens.current.type =="SCANF":
                result.set_child(Parser.parse_scan())

            elif Parser.tokens.current.type == "NUMBER" or Parser.tokens.current.type == "IDENTIFIER":
                result.set_child(Parser.parse_expression())

            elif Parser.tokens.current.type == "DIGIT":
                result.set_child(IntVal(Parser.tokens.current.value))
                Parser.tokens.next()

        else:
            raise ValueError(f"Parse error")

        if Parser.tokens.current.type != "CMD_END":
            raise ValueError(f"Expecting CMD_END token. Got: {Parser.tokens.current.type}")

        Parser.tokens.next()
        return result

    def parse_scan():
        result = 0
        Parser.tokens.next()

        if Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()

            if Parser.tokens.current.type == "CLOSE_PAR":
                result = ScanNode()
                Parser.tokens.next()

            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return result

    def parse_expression():
        result = Parser.parse_term()

        while Parser.tokens.current != None and (Parser.tokens.current.type == "PLUS" or Parser.tokens.current.type == "MINUS"):
            result_cp = result
            result = BinOp(Parser.tokens.current.type)

            Parser.tokens.next()

            result.set_child(result_cp)
            result.set_child(Parser.parse_term())

        return result

    def parse_term():
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
            Parser.tokens.next()
            result = Parser.parse_expression()

            if Parser.tokens.current != None:
                if Parser.tokens.current.type == "CLOSE_PAR":
                    Parser.tokens.next()
                else:
                    raise ValueError(f"Expecting Closing Parenthesis, got: {Parser.tokens.current.type}")

            else:   
                raise ValueError(f"Expecting Closing Parenthesis, got: {Parser.tokens.current.type}")


        else:
            raise ValueError(f"Parse error, got: {Parser.tokens.current.type}")

        return result