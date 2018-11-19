SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1
True equ 1
False equ 0
segment .bss
    x_823a RESD 1
    y_823a RESD 1
    res RESB 1
section .text
    global _start
print:
    POP EBX
    POP EAX
    PUSH EBX
    XOR ESI, ESI
print_dec:
    MOV EDX, 0
    MOV EBX, 0x000A
    DIV EBX
    ADD EDX, '0'
    PUSH EDX
    INC ESI
    CMP EAX, 0
    JZ print_next
    JMP print_dec
print_next:
    CMP ESI, 0
    JZ print_exit
    DEC ESI
    MOV EAX, SYS_WRITE
    MOV EBX, STDOUT
    POP ECX
    MOV [res], ECX
    MOV ECX, res
    MOV EDX, 1
    INT 0x80
    JMP print_next
print_exit:
    RET
binop_je:
    JE binop_true
    JMP binop_false
binop_jg:
    JG binop_true
    JMP binop_false
binop_jl:
    JL binop_true
    JMP binop_false
binop_false:
    MOV EBX, False
    JMP binop_exit
binop_true:
    MOV EBX, True
binop_exit:
    RET
_start:
    MOV EBX, 2
    PUSH EBX
    MOV EBX, 2
    POP EAX
    ADD EAX, EBX
    MOV EBX, EAX
    MOV [x_823a], EBX
    MOV EBX, [x_823a]
    PUSH EBX
    MOV EBX, 6
    POP EAX
    CMP EAX, EBX
    Call binop_jl
    CMP EBX, False
    JE ELSE_74d5
    MOV EBX, [x_823a]
    PUSH EBX
    CALL print
    MOV EBX, 3
    MOV [x_823a], EBX
    JMP EXIT_74d5
    ELSE_74d5:
    MOV EBX, 12345
    PUSH EBX
    CALL print
    EXIT_74d5:
    MOV EBX, 25
    MOV [y_823a], EBX
    LOOP_d458:
    MOV EBX, [y_823a]
    PUSH EBX
    MOV EBX, 10
    POP EAX
    CMP EAX, EBX
    Call binop_jg
    CMP EBX, False
    JE EXIT_d458
    MOV EBX, [y_823a]
    PUSH EBX
    CALL print
    MOV EBX, [y_823a]
    PUSH EBX
    MOV EBX, 1
    POP EAX
    SUB EAX, EBX
    MOV EBX, EAX
    MOV [y_823a], EBX
    JMP LOOP_d458
    EXIT_d458:
    MOV EAX, 1
    INT 0x80
