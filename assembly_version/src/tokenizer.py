from string import ascii_letters, digits
from token import Token

ALLOWED_VARNAME_CHARS = ascii_letters + digits + "_"

RESERVED = {
    "printf" : "PRINT",
    "while" : "WHILE",
    "if" : "IF",
    "else" : "ELSE",
    "scanf": "SCANF",
    "int" : "INT",
    "char" : "CHAR",
    "void" : "VOID",
    "main" : "MAIN",
}

SINGLE_CHAR = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULT",
    "/": "DIV",
    "(": "OPEN_PAR",
    ")": "CLOSE_PAR",
    "{": "OPEN_BLOCK",
    "}": "CLOSE_BLOCK",
    "=": "EQUAL",
    ";": "CMD_END",
    "<": "LESS",
    ">": "GREATER",

}

DOUBLE_CHAR = {
    "==": "EQUALS",
    "<=": "LE",
    ">=": "GE",
    "!=": "DIFFERENT",
    "&&": "AND",
    "||": "OR",
}

class Tokenizer():

    def __init__(self):
        self.origin = "0"
        self.position = 0
        self.current = None

    def _isnumber(self, token):
        return token.isdigit()

    def _isalpha(self, token):
        return token.isalpha()

    def _isdirty(self):
        is_dirty = True
        while is_dirty:
            if self.position < len(self.origin):

                if self.origin[self.position] == " ":
                    self.position += 1

                elif self.origin[self.position] == "/" and self.origin[self.position+1] == "*":
                    while not (self.origin[self.position] == "*" and self.origin[self.position+1] == "/"):
                        if self.position < len(self.origin)-1:  
                            self.position += 1

                        else:
                            raise ValueError("Unterminated Comment")
                    self.position += 2
                
                else:
                    is_dirty = False
            else:
                is_dirty = False

    def next(self):
        aux = ""

        self._isdirty()

        if self.position < len(self.origin):

            if self.position < len(self.origin)-1 and self.origin[self.position]+self.origin[self.position+1] in DOUBLE_CHAR:
                self.current = Token(DOUBLE_CHAR[self.origin[self.position]+self.origin[self.position+1]])
                self.position += 2

            elif self.origin[self.position] in SINGLE_CHAR:
                self.current = Token(SINGLE_CHAR[self.origin[self.position]])
                self.position += 1

            elif self._isnumber(self.origin[self.position]):
                while self._isnumber(self.origin[self.position]):

                    aux += self.origin[self.position]

                    self.position += 1

                    if self.position > len(self.origin)-1:
                        break

                self.current = Token("NUMBER", int(aux))
                aux = ""

            elif self._isalpha(self.origin[self.position]):
                while self.origin[self.position] in ALLOWED_VARNAME_CHARS:

                    aux += self.origin[self.position]

                    self.position += 1

                    if self.position > len(self.origin)-1:
                        break

                if aux in RESERVED:
                    self.current = Token(RESERVED[aux])

                else:
                    self.current = Token("IDENTIFIER", aux)

                aux = ""

            elif self.origin[self.position] == "'" and self.origin[self.position+2] == "'":
                self.current = Token("DIGIT", self.origin[self.position+1])
                self.position += 3


            else:
                raise ValueError(f"invalid token {self.origin[self.position]}")
        else:
            self.current = None