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


class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def __init__(
        self, input_stream: JackTokenizer, output_stream: TextIO
    ) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        self.input_stream: JackTokenizer = input_stream
        self.output_stream: TextIO = output_stream
        self.symble_table: SymbolTable = SymbolTable()
        self.compile_error: Callable[
            [], ValueError
        ] = lambda: ValueError(
            "can't compile this expression{}".format(
                self.input_stream.curr_token
            )
        )
        self.curr_type: str
        self.curr_kind: Literal["ARG", "VAR", "STATIC", "FIELD"]

    def compile_class(self) -> None:
        """Compiles a complete class."""
        self._write_base_token("class", "s")
        self.write_keyword({"class"})
        # write class_name
        self.write_identifier()
        self.write_symbol({"{"})

        while (self.input_stream.token_type() == KEYWORD) and (
            self.input_stream.keyword() in {"static", "field"}
        ):
            self.compile_class_var_dec()

        while (self.input_stream.token_type() == KEYWORD) and (
            self.input_stream.keyword()
            in {"constructor", "function", "method"}
        ):
            self.compile_subroutine()
        self.write_symbol({"}"})
        self._write_base_token("class", "e")

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration.
        "static" | "field" type varName ("," varName)* ";"""

        self._write_base_token("classVarDec", "s")
        self.curr_kind = (
            STATIC
            if self.input_stream.keyword() == "static"
            else FIELD
        )
        self.write_keyword({"static", "field"})
        self._write_type()
        # varName
        self._write_symbol_table()
        self.write_identifier()

        # while curr = ","
        while (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ","
        ):
            self.write_symbol({","})
            # write varName
            self._write_symbol_table()
            self.write_identifier()

        self.write_symbol({";"})
        self._write_base_token("classVarDec", "e")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """

        self.symble_table.start_subroutine()

        self._write_base_token("subroutineDec", "s")
        # constructor or function or method
        self.write_keyword({"constructor", "function", "method"})
        # write type + void
        self._write_type({"void"})
        # subroutine name
        self.write_identifier()
        self.write_symbol({"("})
        self.compile_parameter_list()
        self.write_symbol({")"})
        # subroutine Body
        self.compile_subroutine_body()
        self._write_base_token("subroutineDec", "e")

    def compile_subroutine_body(self) -> None:
        self._write_base_token("subroutineBody", "s")
        self.write_symbol({"{"})

        while (
            self.input_stream.token_type() == KEYWORD
            and self.input_stream.keyword() == "var"
        ):
            self.compile_var_dec()

        self.compile_statements()

        self.write_symbol({"}"})
        self._write_base_token("subroutineBody", "e")

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """
        self._write_base_token("parameterList", "s")
        # if the parameter list is empty
        if (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ")"
        ):
            self._write_base_token("parameterList", "e")
            return

        self.curr_kind = ARG
        self._write_type()
        # varName
        self._write_symbol_table()
        self.write_identifier()

        # aditional parameters
        while (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ","
        ):
            self.write_symbol({","})
            self._write_type()
            # varName
            self._write_symbol_table()

            self.write_identifier()
        self._write_base_token("parameterList", "e")

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""
        self._write_base_token("varDec", "s")
        self.write_keyword({"var"})
        self.curr_kind = VAR
        self._write_type()
        # varName
        self._write_symbol_table()
        self.write_identifier()

        while (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ","
        ):
            self.write_symbol(",")
            self._write_symbol_table()
            self.write_identifier()

        self.write_symbol(";")
        self._write_base_token("varDec", "e")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """
        self._write_base_token("statements", "s")
        while (
            self.input_stream.token_type() == KEYWORD
            and self.input_stream.keyword() in STATEMENT_KEYWORDS
        ):
            if self.input_stream.keyword() == "let":
                self.compile_let()
            elif self.input_stream.keyword() == "if":
                self.compile_if()
            elif self.input_stream.keyword() == "while":
                self.compile_while()
            elif self.input_stream.keyword() == "do":
                self.compile_do()
            elif self.input_stream.keyword() == "return":
                self.compile_return()
            else:
                raise self.compile_error()
        self._write_base_token("statements", "e")

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
        self._write_base_token("letStatement", "s")
        self.write_keyword({"let"})
        if self.input_stream.token_type() == IDENTIFIER:
            self.write_identifier()
            if (
                self.input_stream.token_type() == SYMBOL
                and self.input_stream.symbol() == "["
            ):
                self.write_symbol({"["})
                self.compile_expression()
                self.write_symbol({"]"})
            self.write_symbol({"="})
            self.compile_expression()
            self.write_symbol(";")
        else:
            raise self.compile_error()
        self._write_base_token("letStatement", "e")

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
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ";"
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
            self.input_stream.token_type() == KEYWORD
            and self.input_stream.keyword() == "else"
        ):
            self.write_keyword({"else"})
            self.write_symbol({"{"})
            self.compile_statements()
            self.write_symbol({"}"})
        self._write_base_token("ifStatement", "e")

    def compile_expression(self) -> None:
        """Compiles an expression."""
        self._write_base_token("expression", "s")
        self.compile_term()
        while (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() in OP
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
            self.input_stream.token_type() == INTEGER_CONSTANT
        ):  # integeConstant
            self.write_integer()
        elif (
            self.input_stream.token_type() == STRING_CONSTANT
        ):  # stringConstant
            self.write_string()
        # varname|varname[expression]| subroutineCall
        elif self.input_stream.token_type() == IDENTIFIER:
            if (
                self.input_stream.next_token_val()
                and self.input_stream.next_token_val() in "([."
            ):
                # varname[expression]
                if self.input_stream.next_token_val() == "[":
                    self.write_identifier()
                    self.write_symbol({"["})
                    self.compile_expression()
                    self.write_symbol({"]"})
                elif (
                    self.input_stream.next_token_val() in "(."
                ):  # subroutineCall
                    self._write_callSubroutine()
            else:
                self.write_identifier()
        elif (
            self.input_stream.token_type() == SYMBOL
        ):  # (expression) | unaryOpTerm
            if self.input_stream.symbol() == "(":  # (expression)
                self.write_symbol({"("})
                self.compile_expression()
                self.write_symbol({")"})
            elif (
                self.input_stream.symbol() in UNARY_OP
            ):  # unaryOpTerm
                self.write_symbol(UNARY_OP)
                self.compile_term()
            else:
                raise self.compile_error()
        elif (
            self.input_stream.token_type() == KEYWORD
        ):  # KeywordConstant
            if self.input_stream.keyword() in KYWORD_CONSTANT:
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
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ")"
        ):
            self._write_base_token("expressionList", "e")
            return
        else:
            self.compile_expression()

        while (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == ","
        ):
            self.write_symbol(",")
            self.compile_expression()
        self._write_base_token("expressionList", "e")

    # helper methods:

    def write_symbol(
        self, option_symbol: Union[Set[str], str, None] = None
    ) -> None:
        # check validity
        if self.input_stream.token_type() != SYMBOL:
            raise self.compile_error()
        if (
            option_symbol
            and self.input_stream.symbol() not in option_symbol
        ):
            raise self.compile_error()

        # <symbol>  symbol </symbol>
        self.output_stream.write(
            output_format.format(
                token_type=self.input_stream.token_type(),
                token=self.input_stream.symbol(),
            )
        )

        self.input_stream.advance()

    def write_static_or_field(self) -> None:

        # write <keyword> "static" or "field" </keyword>
        self.output_stream.write(
            output_format.format(
                token_type=self.input_stream.token_type(),
                token=self.input_stream.keyword(),
            )
        )

        self.input_stream.advance()

    def write_identifier(self) -> None:
        # check validity of type
        if self.input_stream.token_type() != IDENTIFIER:
            raise self.compile_error()
        self.output_stream.write(
            output_format.format(
                token_type=self.input_stream.token_type(),
                token=self.input_stream.identifier(),
            )
        )

        self.input_stream.advance()

    def write_keyword(
        self, option_keywards: Optional[Set[str]] = None
    ) -> None:
        # check validity of type
        if self.input_stream.token_type() != KEYWORD:
            raise Exception(
                "Invalid input: in write_keyword method. current type: {} ".format(
                    self.input_stream.token_type()
                )
            )
        if option_keywards:
            if self.input_stream.keyword() not in option_keywards:
                raise Exception(
                    "Invalid input: in write_keyword method. token not in lst, current token: {} ".format(
                        self.input_stream.keyword()
                    )
                )

        self.output_stream.write(
            output_format.format(
                token_type=self.input_stream.token_type(),
                token=self.input_stream.keyword(),
            )
        )

        self.input_stream.advance()

    def write_integer(self) -> None:
        if self.input_stream.token_type() != "integerConstant":
            raise Exception(
                "Invalid input: in write_keyword method. current type: {} ".format(
                    self.input_stream.token_type()
                )
            )

        self.output_stream.write(
            output_format.format(
                token_type=self.input_stream.token_type(),
                token=self.input_stream.int_val(),
            )
        )

        self.input_stream.advance()

    def write_string(self) -> None:
        if self.input_stream.token_type() != "stringConstant":
            raise Exception(
                "Invalid input: in write_string method. current type: {} ".format(
                    self.input_stream.token_type()
                )
            )

        self.output_stream.write(
            output_format.format(
                token_type=self.input_stream.token_type(),
                token=self.input_stream.string_val(),
            )
        )

        self.input_stream.advance()

    def _write_type(self, additional_keywords: Set[str] = set()):
        """Write the type, and update the cuur_type type can be either keyword or identifier
        we can add additional keyword (like void),
        additional_keywords must be form keyword"""
        # is type is keyword int , boolean or char
        types = BASIC_TYPES.union(additional_keywords)
        if (
            self.input_stream.token_type() == KEYWORD
            and self.input_stream.keyword() in types
        ):

            self.curr_type = self.input_stream.keyword()

            self.write_keyword(types)
            # if type is new class
        elif self.input_stream.token_type() == IDENTIFIER:

            self.curr_type = self.input_stream.identifier()

            self.write_identifier()
        else:
            self.compile_error()

    def _write_callSubroutine(self):
        self.write_identifier()
        if (
            self.input_stream.token_type() == SYMBOL
            and self.input_stream.symbol() == "."
        ):
            self.write_symbol({"."})
            self.write_identifier()
        self.write_symbol({"("})
        self.compile_expression_list()
        self.write_symbol({")"})

    def _write_base_token(self, token: str, flog: str):
        if flog == "e":
            self.output_stream.write("</{}>\n".format(token))
        elif flog == "s":
            self.output_stream.write("<{}>\n".format(token))
        else:
            raise ValueError(
                "end must be a string 's' or 'e' it was{}".format(
                    flog
                )
            )

    def _write_symbol_table(self) -> None:
        self.symble_table.define(
            self.input_stream.identifier(),
            self.curr_type,
            self.curr_kind,
        )
