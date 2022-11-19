"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
from enum import Enum #delete?

class Command:

    C_ARITHMETIC = "C_ARITHMETIC"
    C_PUSH = "C_PUSH"
    C_POP = "C_POP"
    C_LABEL = "C_LABEL" 
    C_GOTO = "C_GOTO" 
    C_IF = "C_IF"
    C_FUNCTION = "C_FUNCTION"
    C_RETURN = "C_RETURN" 
    C_CALL = "C_CALL"
 
    # def __init__(self, line : str) -> None:
    #     """Gets ready to parse the input file.

    #     Args:
    #         input_file (typing.TextIO): input file.
    #     """
    #     self.line = line
    #     pass

