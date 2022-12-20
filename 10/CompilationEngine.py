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
keyword = "keyword"
symbol = "symbol"
identifier = "identifier"
ops = { '+', '-', '*', '/', '&', '|', '<', '>','='}

type_lst = {"int", "boolean", "char"}
statsments = {'let', 'do', 'if', 'while', "return"}

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

        self.write_keyword({"class"})

        #write class_name
        self.write_identifier()

        #write_left_curly_brackets
        self.write_symbol("{")
   
        while( (self.input_stream.token_type() == keyword)
        and (self.input_stream.keyword() in {"static", "field"})):
            self.compile_class_var_dec()

        while( (self.input_stream.token_type() == keyword) 
        and (self.input_stream.keyword() in {"constructor", "function", "method"}) ):
            self.compile_subroutine()

        #write_rigth_curly_brackets
        # self.write_symbol("}")

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration."""
        # "static" | "field" type varName ("," varName)* ";"

        self.write_keyword({"static", "field"})

        self.write_keyword({"int", "boolean", "char"})

        #write varName
        self.write_identifier()

        #while curr = ","
        while(self.input_stream.token_type == symbol 
        and self.input_stream.symbol == ","):
            self.write_symbol(",")
            #write varName
            self.write_identifier()

        self.write_symbol(";")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """

        # constructor or function or method (keyword)
        self.write_keyword({"constructor", "function", "method"})

        # type  or void (keyword)
        self.write_keyword({"void", "boolean", "int", "char"})

        # subroutineName (identifier)
        self.write_identifier()

        # "("
        self.write_symbol("(")

        #parameterList
        self.compile_parameter_list()

        # ")"
        self.write_symbol(")")

        #subroutine Body
        self.compile_subroutine_body()

    def compile_subroutine_body(self) -> None:
        # { var dec* statsment}
        self.write_symbol("{")

        while(self.input_stream.token_type() == keyword 
        and self.input_stream.keyword() == "var"):
            self.compile_var_dec()

        self.compile_statements()
        
        self.write_symbol("}")


    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the 
        enclosing "()".
        """
        # Your code goes here!
        pass

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""

        # "var" type varName ("," varName)* ;
        self.write_keyword({"var"})
        self.write_keyword(type_lst)
        self.write_identifier()

        while(self.input_stream.token_type() == symbol 
        and self.input_stream.symbol() == ","):
            self.write_symbol(",")
            self.write_identifier()

        self.write_symbol(";")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing 
        "{}".
        """
        
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
        self.compile_term()
        while(self.input_stream.token_type() == keyword
        and self.input_stream.keyword() in ops):
            self.write_keyword(ops)
            self.compile_term()
        
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
        #integerConstant, StringConstant, keywordConstant
        # Your code goes here!
        pass

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # ( expression (, expression)*)?

        self.write_symbol("(")

        #if not ")"
        if not (self.input_stream.token_type() == symbol 
        and self.input_stream.symbol() == ")"):
            self.compile_expression()

        while (self.input_stream.token_type() == symbol 
        and self.input_stream.symbol() == ","):
            self.write_symbol(",")
            self.compile_expression()
        
        self.write_symbol(")")

    #helper methods:

    def write_symbol(self, symbol : str)->None:
        #check validity
        if(self.input_stream.token_type() != symbol):
            raise Exception("Invalid input: in write_symbol method. current type:{}.".format(self.input_stream.token_type()))

        if (self.input_stream.symbol() != symbol):
            raise Exception(
                "Invalid input: in write_symbol method. current symbol:{}, requested symbol : {}".format(symbol, self.input_stream.symbol()))

        #<symbol>  symbol </symbol>
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type(), 
            token = self.input_stream.symbol()))

        self.input_stream.advance()

    def write_static_or_field(self)->None:

        # write <keyword> "static" or "field" </keyword>
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type(), 
            token = self.input_stream.keyword()))

        self.input_stream.advance()

    def write_identifier(self)->None:
        #check validity of type
        if self.input_stream.token_type() != identifier:
            raise Exception("Invalid input: in write_identifier method. current type: {} "
            .format(self.input_stream.token_type()))
 
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type(), 
            token = self.input_stream.identifier()))

        self.input_stream.advance()

    def write_keyword(self, lst)->None:
        #check validity of type
        if self.input_stream.token_type() != keyword:
            raise Exception("Invalid input: in write_keyword method. current type: {} "
            .format(self.input_stream.token_type()))

        if self.input_stream.keyword() not in lst:
            raise Exception("Invalid input: in write_keyword method. token not in lst, current token: {} "
            .format(self.input_stream.keyword()))
        
        self.output_stream.write(output_format.format(
            token_type = self.input_stream.token_type(), 
            token = self.input_stream.keyword()))

        self.input_stream.advance()
