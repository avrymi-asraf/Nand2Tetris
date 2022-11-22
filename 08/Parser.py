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
    """
    # Parser

    Handles the parsing of a single .vm file, and encapsulates access to the
    input code. It reads VM commands, parses them, and provides convenient 
    access to their components. 
    In addition, it removes all white space and comments.

    ## VM Language Specification

    A .vm file is a stream of characters. If the file represents a
    valid program, it can be translated into a stream of valid assembly 
    commands. VM commands may be separated by an arbitrary number of whitespace
    characters and comments, which are ignored. Comments begin with "//" and
    last until the line’s end.
    The different parts of each VM command may also be separated by an arbitrary
    number of non-newline whitespace characters.

    - Arithmetic commands:
      - add, sub, and, or, eq, gt, lt
      - neg, not, shiftleft, shiftright
    - Memory segment manipulation:
      - push <segment> <number>
      - pop <segment that is not constant> <number>
      - <segment> can be any of: argument, local, static, constant, this, that, 
                                 pointer, temp
    - Branching (only relevant for project 8):
      - label <label-name>
      - if-goto <label-name>
      - goto <label-name>
      - <label-name> can be any combination of non-whitespace characters.
    - Functions (only relevant for project 8):
      - call <function-name> <n-args>
      - function <function-name> <n-vars>
      - return
    """

    def __init__(self, input_file: typing.TextIO) -> None:
        """Gets ready to parse the input file.

        Args:
            input_file (typing.TextIO): input file.
        """
        self.input_lines = input_file.read().splitlines()

        self.input_lines = [
            line.split("//")[0].split("\t")[0] for line in self.input_lines]


        self.input_lines = [
            line for line in self.input_lines if not len(line) == 0]


        self.num_of_commands = len(self.input_lines)
        self.has_more_commands = (self.num_of_commands > 0)
        self.index_of_readen_commands = 0

        if self.has_more_commands:
            self.curr_command = self.input_lines[0]
        else:
            self.curr_command = None

        self.curr_function = "main"

    def advance(self) -> None:
        """Reads the next command from the input and makes it the current 
        command. Should be called only if has_more_commands is true. Initially
        there is no current command.
        """
        
        self.index_of_readen_commands += 1
        if self.index_of_readen_commands < self.num_of_commands:
            self.curr_command = self.input_lines[self.index_of_readen_commands]

            if self.command_type() == "function":
                self.curr_function = self.arg1()

        else:
            self.has_more_commands = False

        if len(self.curr_command) == 0:
            self.advance() 

    def command_type(self) -> str:
        """
        Returns:
            str: the type of the current VM command.
            "C_ARITHMETIC" is returned for all arithmetic commands.
            For other commands, can return:
            "C_PUSH", "C_POP", "C_LABEL", "C_GOTO", "C_IF", "C_FUNCTION",
            "C_RETURN", "C_CALL".
        """

        if self.curr_command == None:
            raise Exception("current command is None")

        word1 = (self.curr_command.split(" "))[0]

        # arithmetic: add, sub, neg, eq, lt, gt, and, or, not
        if word1 in Command.ARITHMETIC_ACTIONS:
            return Command.C_ARITHMETIC

        elif word1 == "push":
            return Command.C_PUSH

        elif word1 == "pop":
            return Command.C_POP

        elif word1 == "label":
            return Command.C_LABEL

        elif word1 == "goto":
            return Command.C_GOTO

        elif word1 == "if-goto":
            return Command.C_IF

        elif word1 == "function":
            return Command.C_FUNCTION

        elif word1 == "return":
            return Command.C_RETURN

        elif word1 == "call":
            return Command.C_CALL

        else:
            raise Exception("Unknown command : {} is undefined ".format(word1))  
                
    def arg1(self) -> str:
        """
        Returns:
            str: the first argument of the current command. In case of 
            "C_ARITHMETIC", the command itself (add, sub, etc.) is returned. 
            Should not be called if the current command is "C_RETURN".
        """
        if self.command_type() == "C_RETURN":
            raise ValueError("return command asked for arg 1")

        if self.command_type() == "":
            raise ValueError("empty command")

        splited_command = self.curr_command.split(" ")

        if self.command_type() in (Command.C_ARITHMETIC):
            # add, sub, neg, eq, lt, gt, and, or, not
            # or label
            return splited_command[0]

        if self.command_type() in (Command.C_PUSH, Command.C_POP, Command.C_LABEL, Command.C_IF) :
            #push, pop
            return splited_command[1]

    def arg2(self) -> int:
        """
        Returns:
            int: the second argument of the current command. Should be
            called only if the current command is "C_PUSH", "C_POP", 
            "C_FUNCTION" or "C_CALL".
        """
        if self.command_type() in (Command.C_POP, Command.C_PUSH, Command.C_FUNCTION, Command.C_CALL):

            splited_command = self.curr_command.split(" ")
            if (len(splited_command) < 2):
                return None
            else:
                return splited_command[2]

    def function(self) -> str:
        """
        Returns:
            int: the second argument of the current command. Should be
            called only if the current command is "C_PUSH", "C_POP", 
            "C_FUNCTION" or "C_CALL".
        """
        return self.curr_function 
