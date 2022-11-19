"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""

import Command
from Command import Command

class SymbolTable:
    """
    A symbol table that keeps a correspondence between symbolic labels and 
    numeric addresses.
    """
        # code  = [
        #     ("C_command":"D=M+1;JLE "),
        #     ("A_command":"12\sss"),
        #     ("L_command":"name"),
        # ]
    
    #empty initialization
    def __init__(self) -> None:
        """Creates a new symbol table initialized with all the predefined symbols
        and their pre-allocated RAM addresses, according to section 6.2.3 of the
        book.
        """
        pass
   

    @staticmethod
    def apply_symbol_table(code : list)->list:
        """
        change in code object
        """
    
        base_symbol_table = {
            "R0":"0",
            "R1":"1",
            "R2":"2",
            "R3":"3",
            "R4":"4",
            "R5":"5",
            "R6":"6",
            "R7":"7",
            "R8":"8",
            "R9":"9",
            "R10":"10",
            "R11":"11",
            "R12":"12",
            "R13":"13",
            "R14":"14",
            "R15":"15",
            "SCREEN":"16384",
            "KBD":"24576",
            "SP":"0",
            "LCL":"1",
            "ARG":"2",
            "THIS":"3",
            "THAT":"4"
            }

        new_symbol_table = {}

        #first loop for finding loops
        for i in range(len(code)):   
            curr_command = code[i]
            if curr_command.command_type == "L_command":
                new_symbol_table[curr_command.command_str] = str(i-len(new_symbol_table))

        new_symbol_table = {**new_symbol_table,**base_symbol_table}

        #second loop
        new_code = []
        count_reg = 16
        for curr_command in code:
            if curr_command.command_type == "A_command":
                if  curr_command.command_str in new_symbol_table:
                    new_command = Command("A_command",new_symbol_table[curr_command.command_str])
                    new_code.append(new_command)
                    # print(new_command)
                elif not curr_command.command_str.isnumeric():
                    new_symbol_table[curr_command.command_str] = str(count_reg)
                    new_command = Command("A_command",str(count_reg))
                    new_code.append(new_command)
                    count_reg+=1
                else:
                    new_code.append(curr_command)
            elif(curr_command.command_type == "L_command"):
                continue
            else:
                new_code.append(curr_command)
        return new_code



