"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
import string


class Command:

    A_COMMAND_STR = "A_command"
    L_COMMAND_STR = "L_command"
    C_COMMAND_STR = "C_command"

    def __init__(self, command_type, command):
        self.command_type = command_type
        self.command_str = str(command)

    def __eq__(self, __o: object) -> bool:
        return ((self.command_str == __o.command_str) and (self.command_type == __o.command_type))
        
    def __str__(self) -> str:
        return self.command_str + "/n"
    

    
    