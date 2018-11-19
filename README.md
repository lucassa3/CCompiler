# CCompiler
Developing a compiler from scratch for C language using python

## How to use:

### AST (Abstract Symbol Table) version:

Simply run:

```
$ python main.py <filename.c>
```
### Assembly generated version:

You need to have nasm installed! To do that. just:
```
$ sudo apt install nasm
```

After that, simply run
```
$ python main.py <filename.c>
```

And if you want to compile you generated asm file:
```
$ nasm -f elf32 -o program.o program.asm
```
```
$ ld -m elf_i386 -s -o program program.o
```

Finally, to execute:

```
$ ./program
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
vardec = type, identifier, ";";

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
