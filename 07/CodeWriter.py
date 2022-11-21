"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
from Codes import Codes
from Command import Command


class CodeWriter:
    """Translates VM commands into Hack assembly code."""

    # TODO add all commands
    aritmetic_commands = {
        "add": Codes.C_add,
        "sub": Codes.C_sub,
        "neg": Codes.C_neg,
        "eq": Codes.C_eq,
        "lt": Codes.C_lt,
        "gt": Codes.C_gt,
        "and": Codes.C_and,
        "or": Codes.C_or,
        "not": Codes.C_not,
        "<<": Codes.C_shiftleft,
        ">>": Codes.C_shiftright
    }

    segments = {
        "local": "LCL",
        "argument": "ARG",
        "this": "THIS",
        "that": "THAT",
        "temp": "TEMP"
    }

    def __init__(self, output_stream: typing.TextIO) -> None:
        """Initializes the CodeWriter.

        Args:
            output_stream (typing.TextIO): output stream.
        """

        self.output_stream = output_stream

        self.file_name = None
        self.counter_label = 1

    def set_file_name(self, filename: str) -> None:
        """Informs the code writer that the translation of a new VM file is 
        started.

        Args:
            filename (str): The name of the VM file.
        """

        # This function is useful when translating code that handles the
        # static segment. For example, in order to prevent collisions between two
        # .vm files which push/pop to the static segment, one can use the current
        # file's name in the assembly variable's name and thus differentiate between
        # static variables belonging to different files.
        # To avoid problems with Linux/Windows/MacOS differences with regards
        # to filenames and paths, you are advised to parse the filename in
        # the function "translate_file" in Main.py using python's os library,
        # For example, using code similar to:
        # input_filename, input_extension = os.path.splitext(os.path.basename(input_file.name))

        self.file_name = filename

        pass

    def write_arithmetic(self, command: str) -> None:
        """Writes assembly code that is the translation of the given 
        arithmetic command. For the commands eq, lt, gt, you should correctly
        compare between all numbers our computer supports, and we define the
        value "true" to be -1, and "false" to be 0.

        Args:
            command (str): an arithmetic command.
        """

        """example: neg
        go to the stack, negate the var 
        - add, sub, and, or, eq, gt, lt
      - neg, not, shiftleft, shiftright
        
        """
        code = self.aritmetic_commands[command]
        if command in ("lt", "gt", "eq"):
            code = code.replace("_counter", str(self.counter_label))
            self.counter_label += 1
        self.output_stream.write(code)

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """Writes assembly code that is the translation of the given 
        command, where command is either C_PUSH or C_POP.

        Args:
            command (str): "C_PUSH" or "C_POP".
            segment (str): the memory segment to operate on.
            index (int): the index in the memory segment.
        """
        # Note: each reference to "static i" appearing in the file Xxx.vm should
        # be translated to the assembly symbol "Xxx.i". In the subsequent
        # assembly process, the Hack assembler will allocate these symbolic
        # variables to the RAM, starting at address 16.

        # Push command:
        # example : push segment index
        # go to segment at the given index, and write it in the top of the stack
        # (sp++, because we increase the stack)

        if command == Command.C_PUSH:

            # push constant
            # example : push constant index
            # take the index as int, and write it in the top of the stack
            # (sp++, because we increase the stack)
            if segment == "constant":
                self.output_stream.write(
                    Codes.push_constant.replace("index", index))

            # push static
            # example : push static i
            # go to static at the symbol "Xxx.i". write it in the top of the stack
            # (sp++, because we increase the stack)
            elif segment == "static":
                self.output_stream.write(Codes.push_static.replace(
                    "index", (self.file_name + "." + str(index))))

            # push pointer
            # example : push pointer 0
            # go to this and write it in the top of the stack
            # (sp++, because we increase the stack)
            elif segment == Command.SEG_POINTER:
                if index == str(0):
                    self.output_stream.write(
                        Codes.push_this_that.replace("index", "THIS"))

                elif index == str(1):
                    self.output_stream.write(
                        Codes.push_this_that.replace("index", "THAT"))

            # push other segment
            elif segment in Command.BASIC_SEGMENTS:
                self.output_stream.write(Codes.push_segment.replace(
                    "index", index).replace("segment", self.segments[segment]))

            elif segment == Command.C_TEMP:
                self.output_stream.write(
                    Codes.push_temp.replace("index", index))

            else:
                # illigal segment
                raise ValueError(
                    "is {} but not segment faund, the given segment is {} .".format(Command.C_PUSH, segment))

        # Pop command:
        # example : pop segment index
        # take the top of the stack (sp--, because we reduce the stack),
        #  and put it inside segment at the given index
        elif command == Command.C_POP:

            # pop other segment
            # example : pop segment index
            # take the top of the stack (sp--, because we reduce the stack),
            # and put it inside segment at the given index

            if segment == Command.C_TEMP:
                self.output_stream.write(Codes.pop_temp.replace("index", index))
            # pop static
            # example : pop static i
            # take the top of the stack (sp--, because we reduce the stack),
            # and put it inside the new static data named (self.file_name + "." + str(index))
            elif segment == Command.SEG_STATIC:
                self.output_stream.write(Codes.pop_static.replace(
                    "index", (self.file_name + "." + str(index))))

            # TODO COMMENT
            # pop pointer
            # example : pop static i
            # take the top of the stack (sp--, because we reduce the stack),
            # and put it inside the new static data named (self.file_name + "." + str(index))
            elif segment == Command.SEG_POINTER:
                if index == 0:
                    self.output_stream.write(
                        Codes.pop_this_that.replace("index", "THIS"))

                elif index == 1:
                    self.output_stream.write(
                        Codes.pop_this_that.replace("index", "THAT"))


            elif segment in Command.BASIC_SEGMENTS:
                self.output_stream.write(Codes.pop_segment.replace(
                    "index", index).replace("segment", self.segments[segment]))

            else:
                # illigal segment
                raise ValueError(
                    "is {} but not segment faund".format(Command.C_POP))

        # illigal segment
        else:
            raise ValueError("illigal command arrived as push_pop command")

    def write_label(self, label: str) -> None:
        """Writes assembly code that affects the label command. 
        Let "Xxx.foo" be a function within the file Xxx.vm. The handling of
        each "label bar" command within "Xxx.foo" generates and injects the symbol
        "Xxx.foo$bar" into the assembly code stream.
        When translating "goto bar" and "if-goto bar" commands within "foo",
        the label "Xxx.foo$bar" must be used instead of "bar".

        Args:
            label (str): the label to write.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        pass

    def write_goto(self, label: str) -> None:
        """Writes assembly code that affects the goto command.

        Args:
            label (str): the label to go to.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        pass

    def write_if(self, label: str) -> None:
        """Writes assembly code that affects the if-goto command. 

        Args:
            label (str): the label to go to.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        pass

    def write_function(self, function_name: str, n_vars: int) -> None:
        """Writes assembly code that affects the function command. 
        The handling of each "function Xxx.foo" command within the file Xxx.vm
        generates and injects a symbol "Xxx.foo" into the assembly code stream,
        that labels the entry-point to the function's code.
        In the subsequent assembly process, the assembler translates this 
        symbol into the physical address where the function code starts.

        Args:
            function_name (str): the name of the function.
            n_vars (int): the number of local variables of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "function function_name n_vars" is:
        # (function_name)       // injects a function entry label into the code
        # repeat n_vars times:  // n_vars = number of local variables
        #   push constant 0     // initializes the local variables to 0
        pass

    def write_call(self, function_name: str, n_args: int) -> None:
        """Writes assembly code that affects the call command. 
        Let "Xxx.foo" be a function within the file Xxx.vm.
        The handling of each "call" command within Xxx.foo's code generates and
        injects a symbol "Xxx.foo$ret.i" into the assembly code stream, where
        "i" is a running integer (one such symbol is generated for each "call"
        command within "Xxx.foo").
        This symbol is used to mark the return address within the caller's 
        code. In the subsequent assembly process, the assembler translates this
        symbol into the physical memory address of the command immediately
        following the "call" command.

        Args:
            function_name (str): the name of the function to call.
            n_args (int): the number of arguments of the function.
        """
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "call function_name n_args" is:
        # push return_address   // generates a label and pushes it to the stack
        # push LCL              // saves LCL of the caller
        # push ARG              // saves ARG of the caller
        # push THIS             // saves THIS of the caller
        # push THAT             // saves THAT of the caller
        # ARG = SP-5-n_args     // repositions ARG
        # LCL = SP              // repositions LCL
        # goto function_name    // transfers control to the callee
        # (return_address)      // injects the return address label into the code
        pass

    def write_return(self) -> None:
        """Writes assembly code that affects the return command."""
        # This is irrelevant for project 7,
        # you will implement this in project 8!
        # The pseudo-code of "return" is:
        # frame = LCL                   // frame is a temporary variable
        # return_address = *(frame-5)   // puts the return address in a temp var
        # *ARG = pop()                  // repositions the return value for the caller
        # SP = ARG + 1                  // repositions SP for the caller
        # THAT = *(frame-1)             // restores THAT for the caller
        # THIS = *(frame-2)             // restores THIS for the caller
        # ARG = *(frame-3)              // restores ARG for the caller
        # LCL = *(frame-4)              // restores LCL for the caller
        # goto return_address           // go to the return address
        pass
