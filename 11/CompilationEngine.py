"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
from collections import Counter
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
import Constants


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
        self.writer: VMWriter = vmWriter
        self.symble_table: SymbolTable = SymbolTable()

        self.curr_type: str = ""
        self.curr_kind: Constants.CurrKindType
        self.curr_class: str = "Main"
        self.curr_subroutine_name: str = ""
        self.counter: Counter[str] = Counter()

    def label_counter(self, label: str) -> str:
        '''
        return label as string with number 

        Args:
            label (str): label

        Returns:
            str: string name name of label with number
        '''
        self.counter[label] += 1
        return label + str(self.counter[label])

    def compile_error(self) -> None:
        raise Exception(
            "can't compile this expression, curr token type: {}, curr token : {}".format(
                self.tokenizer.token_type(), self.tokenizer.curr_token
            )
        )

    def compile_class(self) -> None:
        """Compiles a complete class."""

        # self.symble_table.start_subroutine()
        self.expect_keyword("class")

        # update class_name
        self.curr_class = self.expect_identifier()
        self.expect_symbol("{")
        # while thereis class variable, static or field
        while (self.tokenizer.token_type() == Constants.KEYWORD) and (
            self.tokenizer.keyword()
            in {Constants.STATIC.lower(), Constants.FIELD.lower()}
        ):
            self.compile_class_var_dec()
        # while there is class functions, like constructors, methods, of functions
        while (self.tokenizer.token_type() == Constants.KEYWORD) and (
            self.tokenizer.keyword()
            in {
                Constants.FUNCTION,
                Constants.METHOD,
                Constants.CONSTRUCTOR,
            }
        ):
            self.compile_subroutine()

        self.expect_symbol("}")

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration.
        "static" | "field" type varName ("," varName)* ";"""

        self.curr_kind = self.expect_keyword(Constants.STATIC, Constants.FIELD)  # type: ignore
        self.curr_type = self.expect_keyword(*Constants.BASIC_TYPES)

        # varName
        self._write_symbol_table()

        # while curr = ","
        while (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol(",")

            # write varName
            self._write_symbol_table()

        self.expect_symbol(";")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """

        self.symble_table.start_subroutine()

        self.expect_keyword(*Constants.FUNCTIONS)

        # isMethod = (self.tokenizer.keyword() == "method")

        type: str = self.expect_type()

        # update subroutine name

        self.curr_subroutine_name = (
            self.curr_class + "." + self.expect_identifier()
        )
        self.expect_symbol("(")

        argNuM = self.compile_parameter_list()

        # if isMethod:
        #     self.symble_table.define("this", self.curr_class + self.curr_subroutineName, "arg", 0)

        self.writer.write_function(self.curr_subroutine_name, argNuM)

        self.expect_symbol(")")

        # subroutine Body
        self.compile_subroutine_body()

    def compile_subroutine_body(self) -> None:
        self.expect_symbol("{")
        # var declartion
        while (
            self.tokenizer.token_type() == Constants.KEYWORD
            and self.tokenizer.keyword() == Constants.VAR
        ):
            self.compile_var_dec()

        self.compile_statements()

        self.expect_symbol("}")

    # return the number of parameters
    def compile_parameter_list(self) -> int:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """

        counter = 0

        # if the parameter list is empty
        if (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == ")"
        ):
            return counter

        # if the parameter list NOT empty

        self.curr_kind = Constants.VAR
        self.curr_type = self.expect_keyword(*Constants.BASIC_TYPES)

        # varName
        self._write_symbol_table()
        counter += 1

        # aditional parameters
        while (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            # update type
            self.expect_symbol(",")
            self.curr_type = self.tokenizer.keyword()
            self.tokenizer.advance()

            # update varName
            self._write_symbol_table()
            counter += 1

        return counter

    def compile_var_dec(self) -> None:
        """Compiles a var declaration."""

        self.curr_kind = Constants.segmentsDict[self.expect_keyword(Constants.VAR)]  # type: ignore

        # update current type
        self.curr_type = self.expect_type()

        # varName
        self._write_symbol_table()

        while (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol(",")
            self._write_symbol_table()

        self.expect_symbol(";")

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """

        while (
            self.tokenizer.token_type() == Constants.KEYWORD
            and self.tokenizer.keyword()
            in Constants.STATEMENT_KEYWORDS
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
                self.compile_error()

    def compile_do(self) -> None:
        """Compiles a do statement."""
        # we calld the do statements sometimes insted call subroutines, so only

        self.expect_keyword("do")

        self.compile_expression()
        self.writer.write_pop(Constants.TEMP, 0)
        self.expect_symbol(";")

    def compile_let(self) -> None:
        """Compiles a let statement.
        for example : let x = x+1
        turns to:
        push local 0
        push constant 1
        add
        pop local 0"""
        self.expect_keyword("let")
        # name var

        varToAssignTo: str = self.expect_identifier()

        segmentToAssignTo = self.symble_table.kind_of_as_segment(
            varToAssignTo
        )
        indexToAssignTo: int = self.symble_table.index_of(
            varToAssignTo
        )

        if (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == "["
        ):
            self.expect_symbol("[")
            self.compile_expression()  # TODO FIX
            self.expect_symbol("]")
        self.expect_symbol("=")
        self.compile_expression()

        # pop to var
        self.writer.write_pop(segmentToAssignTo, indexToAssignTo)  # type: ignore

        self.expect_symbol(";")

    def compile_while(self) -> None:
        """Compiles a while statement."""

        # self.write_keyword({"while"})
        # self.write_symbol({"("})
        self.compile_expression()
        # self.write_symbol({")"})
        # self.write_symbol({"{"})
        self.compile_statements()
        # self._write_base_token("whileStatement", "e")

    def compile_return(self) -> None:
        """Compiles a return statement."""

        if not (
            self.tokenizer.next_token_type() == Constants.SYMBOL
            and self.tokenizer.next_token_val() == ";"
        ):

            self.expect_keyword("return")
            self.compile_expression()
        else:
            self.expect_keyword("return")

        self.writer.write_return()
        self.expect_symbol(";")

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # if (expression) {statements}
        label_if_true = self.label_counter("IF_TRUE_")
        label_if_false = self.label_counter("IF_FALSE_")
        label_if_end = self.label_counter("IF_END_")


        self.expect_keyword("if")
        self.expect_symbol("(")
        self.compile_expression()
        self.writer.write_if(label_if_true)
        self.writer.write_goto(label_if_false)
        self.writer.write_label(label_if_true)     
        self.expect_symbol(")")
        self.expect_symbol("{")
        self.compile_statements()
        self.expect_symbol("}")

        if (
            self.tokenizer.token_type() == Constants.KEYWORD
            and self.tokenizer.keyword() == "else"
        ):
            self.writer.write_goto(label_if_end)
            self.writer.write_label(label_if_false)
            self.expect_keyword("else")
            self.expect_symbol("{")
            self.compile_statements()
            self.expect_symbol("}")
            self.writer.write_label(label_if_end)
        else:
            self.writer.write_label(label_if_false)
            

    def compile_expression(self) -> None:
        """Compiles an expression."""

        self.compile_term()

        while (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() in Constants.OP
        ):
            op: Constants.OpType = self.tokenizer.symbol()  # type: ignore
            self.tokenizer.advance()

            self.compile_term()

            self.compile_op(op)

    def compile_op(self, op: Constants.OpType) -> None:
        if op == "*":
            self.writer.write_call("Math.multiply", 2)
        else:
            self.writer.write_arithmetic(op)

    def compile_unary_op(self, op: Constants.UnaryOpType) -> None:
        """
        compile unary operators, some operators like '-' had different command

        Args:
            op (UnaryOpType): operator to write
        """
        self.writer.write_arithmetic("un" + op)

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
        # integeConstant
        if self.tokenizer.token_type() == Constants.INTEGER_CONSTANT:
            self.writer.write_push(
                Constants.CONST, int(self.tokenizer.int_val())
            )
            self.tokenizer.advance()
        # stringConstant
        elif self.tokenizer.token_type() == Constants.STRING_CONSTANT:
            self.writer.write_push_str(self.tokenizer.string_val())
            self.tokenizer.advance()
        # varname|varname[expression]| subroutineCall
        elif self.tokenizer.token_type() == Constants.IDENTIFIER:
            # varname[expression]| subroutineCall
            if (
                self.tokenizer.next_token_val()
                and self.tokenizer.next_token_val() in "([."
            ):
                # varname[expression]
                if self.tokenizer.next_token_val() == "[":
                    # TODO:add method to write array
                    varName: str = self.tokenizer.identifier()
                    self.tokenizer.advance()

                    self.expect_symbol("[")
                    self.compile_expression()
                    self.expect_symbol("]")
                # subroutineCall
                elif self.tokenizer.next_token_val() in "(.":
                    self.compile_subroutineCall()
            # varname
            else:
                var_name: str = self.expect_identifier()
                self.writer.write_push(
                    self.symble_table.kind_of_as_segment(var_name),
                    self.symble_table.index_of(var_name),
                )
        # (expression) | unaryOpTerm
        elif self.tokenizer.token_type() == Constants.SYMBOL:
            if self.tokenizer.symbol() == "(":  # (expression)
                self.expect_symbol("(")
                self.compile_expression()
                self.expect_symbol(")")
            elif (
                self.tokenizer.symbol() in Constants.UNARY_OP
            ):  # unaryOpTerm
                op: Constants.UnaryOpType = self.expect_symbol(*Constants.UNARY_OP)  # type: ignore
                self.compile_term()
                self.compile_unary_op(op)
            else:
                self.compile_error()
        # KeywordConstant
        elif (
            self.tokenizer.token_type() == Constants.KEYWORD
        ):  # TODO what about this
            constant_keyword = self.expect_keyword(
                *Constants.KYWORDS_CONSTANT
            )
            self.writer.write_push(
                # for false and null it 0
                Constants.CONST,
                0,
            )
            if constant_keyword == "true":
                # for true in like thie:
                # push constant 0
                # not

                self.compile_unary_op("~")
        else:
            self.compile_error()

    def compile_expression_list(self) -> int:
        """Compiles a (possibly empty) comma-separated list of expressions."""

        counter = 0

        # if is ")" - continue
        if (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == ")"
        ):
            return counter

        else:
            self.compile_expression()
            counter += 1

        while (
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol(",")
            self.compile_expression()
            counter += 1

        return counter

    #  """helper methods:"""

    def expect_type(self, *additional_keywords) -> str:
        """return the type, and advence the tokenizer
        type can be either keyword or identifier
        we can add additional keyword (like void),
        additional_keywords must be form keyword"""
        # type is keyword int , boolean or char
        if self.tokenizer.token_type() == Constants.KEYWORD:
            return self.expect_keyword(
                *additional_keywords, *Constants.BASIC_TYPES_WITH_VOID
            )
        # if type is a class
        elif self.tokenizer.token_type() == Constants.IDENTIFIER:
            return self.expect_identifier()
        else:
            raise ValueError(
                "expecte type (kyword or identifier) but is not"
            )

    def compile_subroutineCall(self):

        # update subroutine name

        call_subroutineName: str = self.expect_identifier()

        if (  # check if is method call
            self.tokenizer.token_type() == Constants.SYMBOL
            and self.tokenizer.symbol() == "."
        ):
            self.expect_symbol(".")

            # add the rest of the func name
            call_subroutineName += "." + self.expect_identifier()

        self.expect_symbol("(")
        n_args: int = self.compile_expression_list()

        self.writer.write_call(call_subroutineName, n_args)

        self.expect_symbol(")")

    def _write_symbol_table(self) -> None:
        """
        write the current identifier to symbol table
        ane **advance** the tokenizer
        """

        self.symble_table.define(
            self.expect_identifier(),
            self.curr_type,
            self.curr_kind,
        )

    def expect_keyword(self, *keyword) -> Constants.KeywordType:
        """
        check that if current token is keyword
        **advance** token and return the keyword

        Args:
            keyword (_type_): *arg that can be the keyword
        """
        if (self.tokenizer.token_type() != Constants.KEYWORD) or (
            self.tokenizer.keyword() not in keyword
        ):
            self.compile_error()
        ret: Constants.KeywordType = self.tokenizer.keyword()
        self.tokenizer.advance()
        return ret

    def expect_identifier(self) -> str:
        if self.tokenizer.token_type() != Constants.IDENTIFIER:
            self.compile_error()
        ret = self.tokenizer.identifier()
        self.tokenizer.advance()
        return ret

    def expect_symbol(self, *symbol: str) -> Constants.SymbolsType:

        if (self.tokenizer.token_type() != Constants.SYMBOL) or (
            self.tokenizer.symbol() not in symbol
        ):
            self.compile_error()
        ret: Constants.SymbolsType = self.tokenizer.symbol()  # type: ignore
        self.tokenizer.advance()
        return ret
