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
command = assignment | print | commands ;
assignment = identifier , "=" , expression ;
print = "printf" , ( , expression , ) ;
expression = term, { ("+" | "-"), term } ;
term = factor , { ("*" | "/"), factor } ;
factor = ("+" | "-") , factor | "num" | "(" , expression , ")" | identifier ;
identifier = "letter" , { "letter" | "num" | "_" } ;
```
