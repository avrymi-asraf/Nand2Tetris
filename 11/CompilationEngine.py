"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
from typing import (
    Callable,
    Literal,
    Set,
    List,
    TextIO,
    Tuple,
    Optional,
    Union,
)
from JackTokenizer import JackTokenizer
from SymbolTable import SymbolTable
from VMWriter import VMWriter


ARG = "ARG"
VAR = "VAR"

STATIC = "STATIC"
FIELD = "FIELD"


output_format = "<{token_type}> {token} </{token_type}>\n"

KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
VARNAME = IDENTIFIER
INTEGER_CONSTANT = "integerConstant"
STRING_CONSTANT = "stringConstant"
KYWORD_CONSTANT = {"true", "false", "null", "this"}
SYMBOLS = {
    "{",
    "}",
    "(",
    ")",
    "[",
    "]",
    ".",
    ",",
    ";",
    "+",
    "-",
    "*",
    "/",
    "&",
    "|",
    "<",
    ">",
    "=",
    "~",
    "&lt;",
    "&gt;",
    "&amp;",
}
UNARY_OP = {"-", "~", "#", "-"}
OP = {
    "+",
    "-",
    "*",
    "/",
    "<",
    ">",
    "|",
    "&",
    "=",
    "&lt;",
    "&gt;",
    "&amp;",
}
STATEMENT_KEYWORDS = {"let", "if", "while", "do", "return"}
KEYWORDS = {
    "class",
    "constructor",
    "function",
    "method",
    "field",
    "static",
    "var",
    "int",
    "char",
    "boolean",
    "void",
    "true",
    "false",
    "null",
    "this",
    "let",
    "do",
    "if",
    "else",
    "while",
    "return",
}
BASIC_TYPES = {"int", "char", "boolean"}

#TODO FIX
segmentsDict = { STATIC : "static", FIELD : "local",  ARG : "arg", VAR : "local" }

class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def __init__(
        self, tokenizer: JackTokenizer, vmWriter: VMWriter
    ) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        self.tokenizer: JackTokenizer = tokenizer
        self.vmWriter: VMWriter = vmWriter
        self.symble_table: SymbolTable = SymbolTable()

        self.compile_error: Callable[
            [], ValueError
        ] = lambda: ValueError(
            "can't compile this expression{}".format(
                self.tokenizer.curr_token
            )
        )

        self.curr_type: str
        self.curr_kind: Literal["ARG", "VAR", "STATIC", "FIELD"]
        #to keep tracking the current class
        self.curr_class = "Main"

    def compile_class(self) -> None:
        """Compiles a complete class."""
        self.symble_table.start_subroutine()

        self.expect_keyword("class")
        self.tokenizer.advance()

        #update class_name
        self.expect_identifier()
        self.update_class_name()

        self.expect_symbol("{")
        self.tokenizer.advance()

        while (self.tokenizer.token_type() == KEYWORD) and (
            self.tokenizer.keyword() in {"static", "field"}
        ):
            self.compile_class_var_dec()

        while (self.tokenizer.token_type() == KEYWORD) and (
            self.tokenizer.keyword()
            in {"constructor", "function", "method"}
        ):
            self.compile_subroutine()
        self.expect_symbol("}")


    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration.
        "static" | "field" type varName ("," varName)* ";"""

        self.expect_keyword({STATIC, FIELD})
        self.curr_kind = self.tokenizer.keyword()
        self.tokenizer.advance()

        self.expect_keyword(BASIC_TYPES)
        self.curr_type = self.tokenizer.keyword()
        self.tokenizer.advance()

        # varName
        self._write_symbol_table()

        # while curr = ","
        while (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol({","})

            # write varName
            self._write_symbol_table()

        self.expect_symbol({";"})

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """

        self.symble_table.start_subroutine()

        self.expect_keyword({"constructor", "function", "method"})

        isMethod = (self.tokenizer.keyword() == "method")
        
        self.tokenizer.advance()

        self.expect_keyword(BASIC_TYPES + "void")
        self.tokenizer.advance()

        # update subroutine name
        self.expect_identifier()
        self.currFunc = self.tokenizer.identifier()
        self.tokenizer.advance()

        self.expect_symbol("(")

        argNuM = self.compile_parameter_list()

        if isMethod:
            self.symble_table.define("this", self.curr_class + self.currFunc, "arg", 0)

        self.vmWriter.write_function(self.curr_class + self.currFunc, argNuM)

        self.expect_symbol({")"})

        # subroutine Body
        self.compile_subroutine_body()
    

    def compile_subroutine_body(self) -> None:
        self.expect_symbol({"{"})

        while (
            self.tokenizer.token_type() == KEYWORD
            and self.tokenizer.keyword() == "var"
        ):
            self.compile_var_dec()

        self.compile_statements()

        self.expect_symbol("}")

    #return the number of parameters
    def compile_parameter_list(self) -> int:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """

        counter = 0

        # if the parameter list is empty
        if (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ")"
        ):
            return counter

        self.expect_keyword(BASIC_TYPES)    
        self._write_type()
        # varName
        self._write_symbol_table()
        self.write_identifier()
        counter += 1

        # aditional parameters
        while (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.write_symbol({","})
            self._write_type()
            # varName
            self._write_symbol_table()

            self.write_identifier()
            counter += 1
        # self._write_base_token("parameterList", "e")

        return counter

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        
        self.curr_kind = VAR
        self.tokenizer.advance()
        
        #update current type
        self.expect_type()

        # varName
        self._write_symbol_table()
        self.tokenizer.advance()

        while (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol(",")
            self._write_symbol_table()
            self.tokenizer.advance()

        self.expect_symbol(";")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """
        
        while (
            self.tokenizer.token_type() == KEYWORD
            and self.tokenizer.keyword() in STATEMENT_KEYWORDS
        ):
            if self.tokenizer.keyword() == "let":
                self.compile_let()
            elif self.tokenizer.keyword() == "if":
                self.compile_if()
            elif self.tokenizer.keyword() == "while":
                self.compile_while()
            elif self.tokenizer.keyword() == "do":
                self.compile_do()
            elif self.tokenizer.keyword() == "return":
                self.compile_return()
            else:
                raise self.compile_error()
        

    def compile_do(self) -> None:
        """Compiles a do statement."""
        self._write_base_token("doStatement", "s")
        # we calld the do statements sometimes insted call subroutines, so only
        self.write_keyword({"do"})
        self._write_callSubroutine()
        self.write_symbol({";"})
        self._write_base_token("doStatement", "e")

    def compile_let(self) -> None:
        """Compiles a let statement."""

        if self.tokenizer.token_type() == IDENTIFIER:

            token  = self.tokenizer.identifier()

            segment = self.symble_table.kind_of(token)
            index = self.symble_table.index_of(token)
            segment = segmentsDict[segment]

            self.vmWriter.write_push(segment, index)

            self.tokenizer.advance()

            if (
                self.tokenizer.token_type() == SYMBOL
                and self.tokenizer.symbol() == "["
            ):
                self.expect_symbol({"["})
                self.compile_expression() #TODO FIX
                self.expect_symbol({"]"})
            self.expect_symbol({"="})
            self.compile_expression() #TODO FIX
            self.expect_symbol(";")
        else:
            raise self.compile_error()
        

    def compile_while(self) -> None:
        """Compiles a while statement."""
        self._write_base_token("whileStatement", "s")
        self.write_keyword({"while"})
        self.write_symbol({"("})
        self.compile_expression()
        self.write_symbol({")"})
        self.write_symbol({"{"})
        self.compile_statements()
        self.write_symbol({"}"})
        self._write_base_token("whileStatement", "e")

    def compile_return(self) -> None:
        """Compiles a return statement."""
        self._write_base_token("returnStatement", "s")
        self.write_keyword({"return"})
        if not (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ";"
        ):
            self.compile_expression()
        self.write_symbol({";"})
        self._write_base_token("returnStatement", "e")

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        self._write_base_token("ifStatement", "s")
        self.write_keyword({"if"})
        self.write_symbol({"("})
        self.compile_expression()
        self.write_symbol({")"})
        self.write_symbol({"{"})
        self.compile_statements()
        self.write_symbol({"}"})
        if (
            self.tokenizer.token_type() == KEYWORD
            and self.tokenizer.keyword() == "else"
        ):
            self.write_keyword({"else"})
            self.write_symbol({"{"})
            self.compile_statements()
            self.write_symbol({"}"})
        self._write_base_token("ifStatement", "e")

    def compile_expression(self) -> None:
        """Compiles an expression."""
        
        self.compile_term()
        while (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() in OP
        ):
            self.write_symbol(OP)
            self.compile_term()
        self._write_base_token("expression", "e")

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
        self._write_base_token("term", "s")
        if (
            self.tokenizer.token_type() == INTEGER_CONSTANT
        ):  # integeConstant
            self.write_integer()
        elif (
            self.tokenizer.token_type() == STRING_CONSTANT
        ):  # stringConstant
            self.write_string()
        # varname|varname[expression]| subroutineCall
        elif self.tokenizer.token_type() == IDENTIFIER:
            if (
                self.tokenizer.next_token_val()
                and self.tokenizer.next_token_val() in "([."
            ):
                # varname[expression]
                if self.tokenizer.next_token_val() == "[":
                    self.write_identifier()
                    self.write_symbol({"["})
                    self.compile_expression()
                    self.write_symbol({"]"})
                elif (
                    self.tokenizer.next_token_val() in "(."
                ):  # subroutineCall
                    self._write_callSubroutine()
            else:
                self.write_identifier()
        elif (
            self.tokenizer.token_type() == SYMBOL
        ):  # (expression) | unaryOpTerm
            if self.tokenizer.symbol() == "(":  # (expression)
                self.write_symbol({"("})
                self.compile_expression()
                self.write_symbol({")"})
            elif (
                self.tokenizer.symbol() in UNARY_OP
            ):  # unaryOpTerm
                self.write_symbol(UNARY_OP)
                self.compile_term()
            else:
                raise self.compile_error()
        elif (
            self.tokenizer.token_type() == KEYWORD
        ):  # KeywordConstant
            if self.tokenizer.keyword() in KYWORD_CONSTANT:
                self.write_keyword(KYWORD_CONSTANT)
            else:
                raise self.compile_error()
        else:
            raise self.compile_error()
        self._write_base_token("term", "e")

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        self._write_base_token("expressionList", "s")

        # if is ")" - conntine
        if (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ")"
        ):
            self._write_base_token("expressionList", "e")
            return
        else:
            self.compile_expression()

        while (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.write_symbol(",")
            self.compile_expression()
        self._write_base_token("expressionList", "e")

    # helper methods:

    def write_symbol(
        self, option_symbol: Union[Set[str], str, None] = None
    ) -> None:
        # check validity
        if self.tokenizer.token_type() != SYMBOL:
            raise self.compile_error()
        if (
            option_symbol
            and self.tokenizer.symbol() not in option_symbol
        ):
            raise self.compile_error()

        # <symbol>  symbol </symbol>
        self.output_stream.write(
            output_format.format(
                token_type=self.tokenizer.token_type(),
                token=self.tokenizer.symbol(),
            )
        )

        self.tokenizer.advance()

    def write_static_or_field(self) -> None:

        # write <keyword> "static" or "field" </keyword>
        self.output_stream.write(
            output_format.format(
                token_type=self.tokenizer.token_type(),
                token=self.tokenizer.keyword(),
            )
        )

        self.tokenizer.advance()

    def write_identifier(self) -> None:
        # check validity of type
        if self.tokenizer.token_type() != IDENTIFIER:
            raise self.compile_error()
        self.output_stream.write(
            output_format.format(
                token_type=self.tokenizer.token_type(),
                token=self.tokenizer.identifier(),
            )
        )

        self.tokenizer.advance()

    def write_keyword(
        self, option_keywards: Optional[Set[str]] = None
    ) -> None:
        # check validity of type
        if self.tokenizer.token_type() != KEYWORD:
            raise Exception(
                "Invalid input: in write_keyword method. current type: {} ".format(
                    self.tokenizer.token_type()
                )
            )
        if option_keywards:
            if self.tokenizer.keyword() not in option_keywards:
                raise Exception(
                    "Invalid input: in write_keyword method. token not in lst, current token: {} ".format(
                        self.tokenizer.keyword()
                    )
                )

        self.output_stream.write(
            output_format.format(
                token_type=self.tokenizer.token_type(),
                token=self.tokenizer.keyword(),
            )
        )

        self.tokenizer.advance()

    def write_integer(self) -> None:
        if self.tokenizer.token_type() != "integerConstant":
            raise Exception(
                "Invalid input: in write_keyword method. current type: {} ".format(
                    self.tokenizer.token_type()
                )
            )

        self.output_stream.write(
            output_format.format(
                token_type=self.tokenizer.token_type(),
                token=self.tokenizer.int_val(),
            )
        )

        self.tokenizer.advance()

    def write_string(self) -> None:
        if self.tokenizer.token_type() != "stringConstant":
            raise Exception(
                "Invalid input: in write_string method. current type: {} ".format(
                    self.tokenizer.token_type()
                )
            )

        self.output_stream.write(
            output_format.format(
                token_type=self.tokenizer.token_type(),
                token=self.tokenizer.string_val(),
            )
        )

        self.tokenizer.advance()

    def expect_type(self, additional_keywords: Set[str] = set()) -> str:
        """Write the type, and update the cuur_type type can be either keyword or identifier
        we can add additional keyword (like void),
        additional_keywords must be form keyword"""
        # is type is keyword int , boolean or char
        types = BASIC_TYPES.union(additional_keywords)
        if (
            self.tokenizer.token_type() == KEYWORD
            and self.tokenizer.keyword() in types
        ):

            self.curr_type = self.tokenizer.keyword()
            return self.tokenizer.keyword()


            # if type is new class
        elif self.tokenizer.token_type() == IDENTIFIER:

            self.curr_type = self.tokenizer.identifier()
            return self.tokenizer.identifier()

        else:
            self.compile_error()

    def _write_callSubroutine(self):
        self.write_identifier()
        if (
            self.tokenizer.token_type() == SYMBOL
            and self.tokenizer.symbol() == "."
        ):
            self.write_symbol({"."})
            self.write_identifier()
        self.write_symbol({"("})
        self.compile_expression_list()
        self.write_symbol({")"})

    def _write_base_token(self, token: str, flag: str):
        if flag == "e":
            self.output_stream.write("</{}>\n".format(token))
        elif flag == "s":
            self.output_stream.write("<{}>\n".format(token))
        else:
            raise ValueError(
                "end must be a string 's' or 'e' it was{}".format(
                    flag
                )
            )

    def _write_symbol_table(self) -> None:
        self.symble_table.define(
            self.tokenizer.identifier(),
            self.curr_type,
            self.curr_kind,
        )


    #this method is to keep tracking the current class name
    def update_class_name(self) -> None:
        # check validity of type
        if self.tokenizer.token_type() != IDENTIFIER:
            self.compile_error()
            return
        self.curr_class = self.tokenizer.identifier()
        self.tokenizer.advance()


    def expect_keyword(self, keyword: set(str)):
        if ((self.tokenizer.token_type() != KEYWORD)
         or (self.tokenizer.keyword() != keyword)):
            self.compile_error()

    def expect_symbol(self, symbol: str):
        if ((self.tokenizer.token_type() != SYMBOL)
         or (self.tokenizer.symbol() != symbol)):
            self.compile_error()
        self.tokenizer.advance()
            
    def expect_identifier(self):
        if (self.tokenizer.token_type() != IDENTIFIER):
            self.compile_error()




