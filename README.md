# CCompiler
Developing a compiler from scratch for C language

## How to use:

Simply run:

```
$ python main.py <filename.c>
```

* Note: for compatibility reasons, its important to haver python 3.6 or above installed.

## EBNF:

```ebnf
program = "void", "main", "(", ")", commands;
commands = "{", {command}, "}" ;
command = assignment | print | if_else | while | commands | vardec;

assignment = identifier , "=" , (expression | scanf), ";";
print = "printf" , "(", expression , ")", ";";
if_else = "if", "(", bool_exp, ")", commands, ["else", commands];
while = "while", "(", bool_exp, ")", commands;
vardec = "INT", identifier, ";"

bool_exp = bool_term, {"or", bool_term}; 
bool_term = bool_factor, {"and", bool_factor};
bool_factor =  ("not", bool_factor) | rel_expr;
rel_expr = expression, {("<" | ">" | "=="), expression};
expression = term, { ("+" | "-"), term };
term = factor , { ("*" | "/"), factor };
factor = (("+" | "-") , factor) | num | ("(" , expression , ")") | identifier;

scanf = "scanf", "(", ")";
identifier = letter, { letter | digit | "_" };
num = digit, {digit};
letter = "a" .. "Z";
digit = "0" .. "9";
type = "void" | "int" | "char";
```

## Syntax Diagrams

![Alt text](imgs/syntax_diagram.png?raw=true "SYNTAX DIAGRAM")