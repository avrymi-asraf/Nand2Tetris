"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
from typing import TextIO
import Constants


class VMWriter:
    """
    Writes VM commands into a file. Encapsulates the VM command syntax.
    """

    def __init__(self, output_stream: TextIO) -> None:
        """Creates a new file and prepares it for writing VM commands."""
        # Your code goes here!
        # Note that you can write to output_stream like so:
        # output_stream.write("Hello world! \n")

        self.output_stream: TextIO = output_stream

    def write_push(self, segment: Constants.SegmentType, index: int) -> None:
        """Writes a VM push command.

        Args:
            segment (str): the segment to push to, can be "CONST", "ARG",
            "LOCAL", "STATIC", "THIS", "THAT", "POINTER", "TEMP"
            index (int): the index to push to.
        """
        # check validity
        if segment not in {
            Constants.CONST,
            Constants.ARG,
            Constants.LOCAL,
            Constants.STATIC,
            Constants.THIS,
            Constants.THAT,
            Constants.POINTER,
            Constants.TEMP,
        }:
            self.write_error(segment + " " + str(index))

        self.output_stream.write(
            "push {} {}\n".format(segment.lower(), index)
        )

    def write_pop(self, segment: str, index: int) -> None:
        """Writes a VM pop command.

        Args:
            segment (str): the segment to pop from, can be "CONST", "ARG",
            "LOCAL", "STATIC", "THIS", "THAT", "POINTER", "TEMP".
            index (int): the index to pop from.
        """
        # check validity
        if segment not in {
            "CONST",
            "ARG",
            "LOCAL",
            "STATIC",
            "THIS",
            "THAT",
            "POINTER",
            "TEMP",
        }:
            self.write_error(segment + " " + str(index))

        self.output_stream.write(
            "pop {} {}\n".format(segment.lower(), index)
        )

    def write_arithmetic(self, command: str) -> None:
        """Writes a VM arithmetic command.

        Args:
            command (str): the command to write, can be "ADD", "SUB", "NEG",
            "EQ", "GT", "LT", "AND", "OR", "NOT", "SHIFTLEFT", "SHIFTRIGHT".
        """
        # check validity
        if command.upper() not in {
            "ADD",
            "SUB",
            "NEG",
            "EQ",
            "GT",
            "LT",
            "AND",
            "OR",
            "NOT",
            "SHIFTLEFT",
            "SHIFTRIGHT",
        }:
            self.write_error(command)

        self.output_stream.write(f'{command}\n')

    def write_label(self, label: str) -> None:
        """Writes a VM label command.

        Args:
            label (str): the label to write.
        """
        self.output_stream.write("label {}\n".format(label))

    def write_goto(self, label: str) -> None:
        """Writes a VM goto command.

        Args:
            label (str): the label to go to.
        """
        self.output_stream.write("goto {}\n".format(label))

    def write_if(self, label: str) -> None:
        """Writes a VM if-goto command.

        Args:
            label (str): the label to go to.
        """
        self.output_stream.write("if-goto {}\n".format(label))

    def write_call(self, name: str, n_args: int) -> None:
        """Writes a VM call command.

        Args:
            name (str): the name of the function to call.
            n_args (int): the number of arguments the function receives.
        """
        self.output_stream.write("call {} {}\n".format(name, n_args))

    def write_function(self, name: str, n_locals: int) -> None:
        """Writes a VM function command.

        Args:
            name (str): the name of the function.
            n_locals (int): the number of local variables the function uses.
        """
        self.output_stream.write(
            "function {} {}\n".format(name, n_locals)
        )

    def write_return(self) -> None:
        """Writes a VM return command."""
        self.output_stream.write("return\n")

    def write_error(self, val: str) -> None:
        """Writes a VM return command."""
        raise Exception("can't write this expression: {}".format(val))

    def write_push_str(self, val: str) -> None:
        '''
        write string object 

        Args:
            val (str): string to write
        '''        
        self.write_push(Constants.CONST,len(val))
        self.write_call("String.new",1)
        for char in val:
            self.write_push(Constants.CONST,ord(char))
            self.write_call("String.appendChar",2)


