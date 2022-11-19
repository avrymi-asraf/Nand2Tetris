from SymbolTable import apply_symbol_table
from Parser import Parser, COMMAND

code = [
    ("A_command", "0"),
    ("C_command", "D=M"),
    ("A_command", "INFINITE_LOOP"),
    ("C_command", "D;JLE"),
    ("A_command", "counter"),
    ("C_command", "M=D"),
    ("A_command", "SCREEN"),
    ("C_command", "D=A"),
    ("A_command", "address"),
    ("C_command", "M=D"),
    ("L_command", "LOOP"),
    ("A_command", "address"),
    ("C_command", "A=M"),
    ("C_command", "M=-1"),
    ("A_command", "address"),
    ("C_command", "D=M"),
    ("A_command", "32"),
    ("C_command", "D=D+A"),
    ("A_command", "address"),
    ("C_command", "M=D"),
    ("A_command", "counter"),
    ("C_command", "MD=M-1"),
    ("A_command", "LOOP"),
    ("C_command", "D;JGT"),
    ("L_command", "INFINITE_LOOP"),
    ("A_command", "INFINITE_LOOP"),
    ("C_command", "0;JMP")

]


# new_code = aplly_symbol_table(code)
# # print(new_code)

# with open('out', 'w') as fp:
#     for item in new_code:
#         # write each item on a new line
#         fp.write("\n" + str(item))

with open('rect\Rect.asm', 'r') as fp:
    pra = Parser(fp)