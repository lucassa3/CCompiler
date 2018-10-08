# CCompiler
Developing a compiler from scratch for C language


![Alt text](imgs/commands.png?raw=true "Title")
![Alt text](imgs/command.png?raw=true "Title")
![Alt text](imgs/assignment.png?raw=true "Title")
![Alt text](imgs/print.png?raw=true "Title")
![Alt text](imgs/diagram_01.png?raw=true "Title")
![Alt text](imgs/diagram_02.png?raw=true "Title")
![Alt text](imgs/diagram_03.png?raw=true "Title")
![Alt text](imgs/diagram_04.png?raw=true "Title")



```ebnf
commands = "{", command, ";", { command, ";" }, "}" ;
command = assignment | print | if_else | while | commands ;
assignment = identifier , "=" , (expression | scanf);
scanf = "scanf", "(", ")";
print = "printf" , ( , expression , ) ;
rel_expr = expression, {("<" | ">" | "=="), expression};
if = "if", "(", rel_expr, ")", "{", statement, "}" , ["else", "{" statement, "}"];
while = "while", "(", rel_expr, ")", "{", statement, "}" , ["else", "{" statement, "}"];
expression = term, { ("+" | "-"), term } ;
term = factor , { ("*" | "/"), factor } ;
factor = ("+" | "-") , factor | num | "(" , expression , ")" | identifier ;
identifier = word, { word | num | "_" } ;
num = digit, {digit} ;
word = letter, {letter} ;
letter = a .. z | A .. Z;
digit = 0 .. 9;
type = "bool" | "integer";
```
