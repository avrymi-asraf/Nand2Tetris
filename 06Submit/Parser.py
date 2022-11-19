"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
import Command
from Command import Command


class Parser:
    """Encapsulates access to the input code. Reads an assembly program
    by reading each command line-by-line, parses the current command,
    and provides convenient access to the commands components (fields
    and symbols). In addition, removes all white space and comments.
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Opens the input file and gets ready to parse it.

        Args:
            input_file (typing.TextIO): input file.
        """

        #create code list
        self.commands_list:list(Command) = []

        #split the input file into lines
        self.input_lines = input_file.read().splitlines()

        #check line by line
        for line in self.input_lines :
            #enter new line with no spaces
            line = line.strip()
            line = line.replace(" ", "") 
            line = line.replace("//", "#")
            line = line.split("#")[0]

            #add the line to the commands list
            if (len(line) > 0):
                command_type =  self.find_command_type(line)
                line = line.replace("@","")
                line = line.replace("(","")
                line = line.replace(")","")
                self.commands_list.append(Command(command_type, line))

        
    #find command type        
    def find_command_type(self, word) -> str:

        """
        Returns:
            str: the type of the current command:
            "A_COMMAND" for @Xxx where Xxx is either a symbol or a decimal number
            "C_COMMAND" for dest=comp;jump
            "L_COMMAND" (actually, pseudo-command) for (Xxx) where Xxx is a symbol
        """
    
        if (word[0] == "@"):
            return Command.A_COMMAND_STR
            
        elif (word[0] == "(") and (word[len(word) -1] == ")"):
            return Command.L_COMMAND_STR

        elif ((word[0] == "M") or (word[0] == "D") or (word[0] == "A") or (word[0] == "0")):
            return Command.C_COMMAND_STR
