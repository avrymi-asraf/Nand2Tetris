"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
# import typing
import Command

class Code:
    """Translates Hack assembly language mnemonics into binary codes."""


    @staticmethod
    def var(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a decimal representation of integer

        Returns:
            str: binary code of the given representation
        """
        num = int(mnemonic)
        return bin(num)[2:].zfill(15)

    
    @staticmethod
    def dest(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a dest mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        result = {"null": "000",
                  "M": "001",
                  "D": "010",
                  "MD": "011",
                  "A": "100",
                  "AM": "101",
                  "AD": "110",
                  "AMD": "111"}
        return result[mnemonic]

    @staticmethod
    def comp(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a comp mnemonic string.

        Returns:
            str: the binary code of the given mnemonic.
        """
        result = {"0": "101010",
                  "1": "111111",
                  "-1":"111010",
                  "D": "001100",
                  "A": "110000",
                  "M": "110000",
                  "!D": "001101",
                  "!A": "110001",
                  "!M": "110001",
                  "-D": "001111",
                  "-A": "110011",
                  "-M": "110011",
                  "D+1": "011111",
                  "A+1": "110111",
                  "M+1": "110111",
                  "D-1": "001110",
                  "A-1": "110010",
                  "M-1": "110010",
                  "D+A": "000010",
                  "D+M": "000010",
                  "D-A": "010011",
                  "D-M": "010011",
                  "A-D": "000111",
                  "M-D": "000111",
                  "D&A": "000000",
                  "D&M": "000000",
                  "D|A": "010101",
                  "D|M": "010101",
                  "A<<": "100000",
                  "D<<": "110000",
                  "M<<": "100000",
                  "A>>": "000000",
                  "D>>": "010000",
                  "M>>": "000000",
                  }
        return result[mnemonic]

    @staticmethod
    def jump(mnemonic: str) -> str:
        """
        Args:
            mnemonic (str): a jump mnemonic string.

        Returns:
            str: 3-bit long binary code of the given mnemonic.
        """
        result = {"null": "000",
                  "JGT": "001",
                  "JEQ": "010",
                  "JGE": "011",
                  "JLT": "100",
                  "JNE": "101",
                  "JLE": "110",
                  "JMP": "111"}
        return result[mnemonic]

 
#translate single command to binary representation       
def command_to_bin_str(command: Command) -> str:

    c_command_prefix = "111"
    inc_M_flag = "0"

    #in case of A command
    if command.command_type == "A_command":
        return "0" + Code.var(command.command_str)

    #in case of C command
    elif command.command_type == "C_command":

        if "=" in command.command_str:
            assem_dest :str  = command.command_str.split("=")[0]
            assem_comp_n_jmp :str  = command.command_str.split("=")[1]
            
        if not "=" in command.command_str:
            assem_dest :str  = "null"
            assem_comp_n_jmp :str  = command.command_str


        if ";" in assem_comp_n_jmp:
            #check if there is a jmp, if not - null
            assem_lst = assem_comp_n_jmp.split(";")
            if len(assem_lst) > 1:
                assem_comp:str  = assem_comp_n_jmp.split(";")[0]
                assem_jmp:str  = assem_comp_n_jmp.split(";")[1]

            elif len(assem_lst) <=1 :
                assem_comp:str  = assem_comp_n_jmp.split(";")[0]
                assem_jmp:str  = "null"


        if not ";" in assem_comp_n_jmp:
            assem_comp:str  = assem_comp_n_jmp
            assem_jmp:str  = "null"

        #convert to binary representation
        bin_dest = Code.dest(assem_dest)
        bin_comp = Code.comp(assem_comp)
        bin_jmp = Code.jump(assem_jmp)

        #check if M is in memory
        if "M" in assem_comp:
            inc_M_flag ="1"

        #check if the copm is shifted
        if (">>" in assem_comp) or "<<" in assem_comp:
            c_command_prefix = "101"

        joined_command = c_command_prefix + inc_M_flag + bin_comp + bin_dest + bin_jmp
        return joined_command