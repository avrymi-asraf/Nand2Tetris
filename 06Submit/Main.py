"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
import SymbolTable
from SymbolTable import SymbolTable
import Parser
from Parser import Parser
import Code
import Command


def assemble_file(
        input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """Assembles a single file.

    Args:
        input_file (typing.TextIO): the file to assemble.
        output_file (typing.TextIO): writes all output to this file.
    """


    #create code list
    new_parser:Parser = Parser(input_file)
    command_list:typing.list(Command) = new_parser.commands_list
    new_symbol_table = SymbolTable()
    assembly_final_code = new_symbol_table.apply_symbol_table(command_list)
    
    #write to output file
    for command in assembly_final_code:
        bin_command = Code.command_to_bin_str(command)
        output_file.write(bin_command)
        # output_file.write(command.command_str)
        output_file.write('\n')
    
    
if "__main__" == __name__:
    # Parses the input path and calls assemble_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: Assembler <input path>")

    # print("got to before parser") #delete

    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".asm":
            continue
        output_path = filename + ".hack"
       
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            assemble_file(input_file, output_file)
            
            




