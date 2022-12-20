"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing
from JackTokenizer import JackTokenizer

output_format = "<{token_type}> {token} </{token_type}>\n"

class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    #TODO why output stream is not of type typing.TextIO?
    def __init__(self, input_stream: JackTokenizer, output_stream) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        self.input_stream = input_stream
        self.output_stream = output_stream
        
    def compile_class(self) -> None:
        """Compiles a complete class."""

        self.write_class()

        #write_class_name
        self.write_identifier()

        #write_left_curly_brackets
        self.write_symbol(self, "{")

        while( (self.input_stream.token_type() == "KEYWORDS")
        and (self.input_stream.keyword() in  {"static", "field"})):
            self.compile_var_dec()

        while( (self.input_stream.token_type() == "KEYWORDS") 
        and (self.input_stream.keyword() in {"constructor", "function", "method"}) ):
            self.compile_subroutine()

        #write_rigth_curly_brackets
        self.write_symbol(self, "}")

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        # "static" | "field" type varName ("," varName)* ";"

        self.write_static_or_field()

        self.write_type()

        #write varName
        self.write_identifier()

        #while curr = ","
        while(self.input_stream.token_type == "SYMBOL" 
        and self.input_stream.symbol == ","):
            self.write_symbol(self, ",")
            #write varName
            self.write_identifier()

        self.write_symbol(self, ";")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """

        
        



        pass

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the 
        enclosing "()".
        """
        # Your code goes here!
        pass

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        # Your code goes here!
        pass

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing 
        "{}".
        """
        # Your code goes here!
        pass

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # Your code goes here!
        pass

    def compile_let(self) -> None:
        """Compiles a let statement."""
        # Your code goes here!
        pass

    def compile_while(self) -> None:
        """Compiles a while statement."""
        # Your code goes here!
        pass

    def compile_return(self) -> None:
        """Compiles a return statement."""
        # Your code goes here!
        pass

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!
        pass

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        pass

    def compile_term(self) -> None:
        """Compiles a term. 
        This routine is faced with a slight difficulty when
        trying to decide between some of the alternative parsing rules.
        Specifically, if the current token is an identifier, the routing must
        distinguish between a variable, an array entry, and a subroutine call.
        A single look-ahead token, which may be one of "[", "(", or "." suffices
        to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        # Your code goes here!
        pass

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # Your code goes here!
        pass


    #helper methods:

    def write_class(self)->None:
        if (self.input_stream.token_type == "KEYWORD" 
        and self.input_stream.keyword == "class"):
            raise Exception("in write class - not starts with class")

        #<keyword> class </keyword>
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type().lower(), token = "class"))

        self.input_stream.advance()
        return

    def write_symbol(self, symbol : str)->None:
        #check validity
        if( (self.input_stream.token_type != "SYMBOL") or 
        (self.input_stream.symbol() != symbol)) : 
            raise Exception("in compile_class method - not a symbol")

        #<symbol> } </symbol>
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type().lower(), 
            token = self.input_stream.symbol()))

        self.input_stream.advance()

    def write_static_or_field(self)->None:

        # write <keyword> "static" or "field" </keyword>
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type().lower(), 
            token = self.input_stream.keyword()))

        self.input_stream.advance()

    def write_type(self)->None:
        #check validity of type
        if not ( (self.input_stream.token_type == "KEYWORD" 
        and self.input_stream.keyword() in {"char", "int", "boolean"})
        or (self.input_stream.token_type == "IDENTIFIER")):
            raise Exception("in compile_class var dec method - not a type")
 
        # write <keyword> type </keyword>
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type().lower(), 
            token = self.input_stream.keyword()))
        
        self.input_stream.advance()

    def write_identifier(self)->None:
        #check validity of type
        if not self.input_stream.token_type == "IDENTIFIER":
            raise Exception("in write_identifier method - not a identifier")
 
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type().lower(), 
            token = self.input_stream.identifier()))

        self.input_stream.advance()