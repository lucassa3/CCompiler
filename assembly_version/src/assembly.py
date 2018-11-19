CONSTANTS = [
    "SYS_EXIT equ 1",
    "SYS_READ equ 3",
    "SYS_WRITE equ 4",
    "STDIN equ 0",
    "STDOUT equ 1",
    "True equ 1",
    "False equ 0"
]


PRINT_PROC = [
    "section .text",
    "    global _start",
    "print:",
    "    POP EBX",
    "    POP EAX",
    "    PUSH EBX",
    "    XOR ESI, ESI",
    "print_dec:",
    "    MOV EDX, 0",
    "    MOV EBX, 0x000A",
    "    DIV EBX",
    "    ADD EDX, '0'",
    "    PUSH EDX",
    "    INC ESI",
    "    CMP EAX, 0",
    "    JZ print_next",
    "    JMP print_dec",
    "print_next:",
    "    CMP ESI, 0",
    "    JZ print_exit",
    "    DEC ESI",
    "    MOV EAX, SYS_WRITE",
    "    MOV EBX, STDOUT",
    "    POP ECX",
    "    MOV [res], ECX",
    "    MOV ECX, res",
    "    MOV EDX, 1",
    "    INT 0x80",
    "    JMP print_next",
    "print_exit:",
    "    RET"
]

IF_WHILE_PROC = [
    "binop_je:",
    "    JE binop_true",
    "    JMP binop_false",
    "binop_jg:",
    "    JG binop_true",
    "    JMP binop_false",
    "binop_jl:",
    "    JL binop_true",
    "    JMP binop_false",
    "binop_false:",
    "    MOV EBX, False",
    "    JMP binop_exit",
    "binop_true:",
    "    MOV EBX, True",
    "binop_exit:",
    "    RET"
]

INTERRUPT = [
    "    MOV EAX, 1",
    "    INT 0x80"
]


class Assembly():
    assembly = [
    ]

    bss_segment = [
        "segment .bss"
    ]

    program = [
        "_start:"
    ]

    def write_program(lines):
        for line in lines:
            Assembly.program.append("    " + line)

    def write_bss(line):
        Assembly.bss_segment.append("    " + line)

    def build_file():
        Assembly.assembly.extend(CONSTANTS)
        Assembly.bss_segment.append("    " + "res RESB 1")
        Assembly.assembly.extend(Assembly.bss_segment)
        Assembly.assembly.extend(PRINT_PROC)
        Assembly.assembly.extend(IF_WHILE_PROC)
        Assembly.assembly.extend(Assembly.program)
        Assembly.assembly.extend(INTERRUPT)

        with open("program.asm", "w") as myfile:
            for line in Assembly.assembly:
                myfile.write(line + "\n")
