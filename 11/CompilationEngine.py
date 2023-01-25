"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
from collections import Counter
from re import A
from JackTokenizer import JackTokenizer
from SymbolTable import SymbolTable
from VMWriter import VMWriter
import cons


class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def __init__(self, tokenizer: JackTokenizer, vmWriter: VMWriter) -> None:
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
        self.curr_kind: cons.VarKindType
        self.curr_class: str = "Main"
        self.curr_subroutine_name: str = ""
        self.counter: Counter[str] = Counter()

    def label_counter(self, label: str) -> str:
        """
        return label as string with number

        Args:
            label (str): label

        Returns:
            str: string name name of label with number
        """
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
        while (self.tokenizer.token_type() == cons.KEYWORD) and (
            self.tokenizer.keyword() in {cons.STATIC.lower(), cons.FIELD.lower()}
        ):
            self.compile_class_var_dec()
        # while there is class functions, like constructors, methods, of functions
        while (self.tokenizer.token_type() == cons.KEYWORD) and (
            self.tokenizer.keyword()
            in {
                cons.FUNCTION,
                cons.METHOD,
                cons.CONSTRUCTOR,
            }
        ):
            self.compile_subroutine()

        self.expect_symbol("}")

    def compile_class_var_dec(self) -> None:
        """Compiles a static declaration or a field declaration.
        "static" | "field" type varName ("," varName)* ";"""

        self.curr_kind = self.expect_keyword(cons.STATIC, cons.FIELD)  # type: ignore
        self.curr_type = self.expect_type()

        # varName
        self._write_symbol_table()

        # while curr = ","
        while (
            self.tokenizer.token_type() == cons.SYMBOL
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

        func_type: cons.FunctionType = self.expect_keyword(*cons.FUNCTIONS)  # type: ignore , keyword most be function

        if func_type == cons.METHOD:
            self.symble_table.define(self.curr_class, cons.THIS, cons.ARG)
        # type of function
        self.expect_type()

        # update subroutine name
        self.curr_subroutine_name = self.curr_class + "." + self.expect_identifier()
        self.expect_symbol("(")

        argNuM = self.compile_parameter_list()

        self.expect_symbol(")")
        # subroutine Body
        self.expect_symbol("{")
        # var declartion
        var_counter: int = 0
        while (
            self.tokenizer.token_type() == cons.KEYWORD
            and self.tokenizer.keyword() == cons.VAR
        ):
            var_counter += self.compile_var_dec()

        # write furnction with number of locals variables
        self.writer.write_function(self.curr_subroutine_name, var_counter)
        if func_type == cons.METHOD:
            self.writer.write_push(cons.kind_to_segment[cons.ARG], 0)
            self.writer.write_pop(cons.kind_to_segment[cons.POINTER], 0)
        elif func_type == cons.CONSTRUCTOR:
            self.writer.write_push(
                cons.CONST, self.symble_table.num_of_kind(cons.FIELD)
            )
            self.writer.write_call("Memory.alloc", 1)
            self.writer.write_pop(cons.POINTER, 0)

        self.compile_subroutine_body()

    def compile_subroutine_body(self) -> None:
        """
        compile the subroutine body
        without var declarations that compile in compile_subroutine function
        """
        self.compile_statements()
        self.expect_symbol("}")

    def compile_parameter_list(self) -> int:
        """
        compile a parameter list
        add arguments to symbol table and return number of arguments
        """

        counter: int = 0

        # if the parameter list is empty
        if (
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == ")"
        ):
            return counter

        # if the parameter list NOT empty

        self.curr_kind = cons.ARG
        self.curr_type = self.expect_type()

        # varName
        self._write_symbol_table()
        counter += 1

        # aditional parameters
        while (
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            # update type
            self.expect_symbol(",")
            self.curr_type = self.expect_type()
            # update varName
            self._write_symbol_table()
            counter += 1

        return counter

    def compile_var_dec(self) -> int:
        """
        Compiles a var declaration
        for seme type and return number variables
        """
        counter: int = 0
        self.curr_kind = self.expect_keyword(cons.VAR)  # type: ignore keyword most be in VarKindType

        # update current type
        self.curr_type = self.expect_type()

        # varName
        self._write_symbol_table()
        counter += 1

        while (
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol(",")
            self._write_symbol_table()
            counter += 1

        self.expect_symbol(";")
        return counter

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """

        while (
            self.tokenizer.token_type() == cons.KEYWORD
            and self.tokenizer.keyword() in cons.STATEMENT_KEYWORDS
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
        self.writer.write_pop(cons.TEMP, 0)
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

        segmentToAssignTo: cons.SegmentType = self.symble_table.kind_of_as_segment(
            varToAssignTo
        )
        indexToAssignTo: int = self.symble_table.index_of(varToAssignTo)

        if (
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == "["
        ):
            arr_segment: cons.SegmentType = segmentToAssignTo
            arr_index: int = indexToAssignTo

            # arr[i] = expression
            # 1.
            # 2. push arr
            # 3. compile_expression
            # 4. add
            # 5. compile_expression
            # 6. compile_expression (to put in arr)
            # 8. pop to temp
            # 9.
            self.expect_symbol("[")
            self.compile_expression()
            self.expect_symbol("]")
            self.writer.write_push(arr_segment, arr_index)
            self.writer.write_arithmetic("+")
            self.expect_symbol("=")
            self.compile_expression()
            self.writer.write_pop(cons.TEMP, 0)
            self.writer.write_pop(cons.POINTER, 1)
            self.writer.write_push(cons.TEMP, 0)
            self.writer.write_pop(cons.THAT, 0)
        else:
            self.expect_symbol("=")
            self.compile_expression()
            # pop to var
            self.writer.write_pop(segmentToAssignTo, indexToAssignTo)  # type: ignore

        self.expect_symbol(";")

    def compile_while(self) -> None:
        """Compiles a while statement."""
        start_label = self.label_counter("START_WHILE_")
        if_label = self.label_counter("IF_WHILE_")
        end_label = self.label_counter("END_WHILE_")

        self.expect_keyword("while")
        self.writer.write_label(start_label)
        self.expect_symbol("(")
        self.compile_expression()
        self.expect_symbol(")")
        self.writer.write_if(if_label)
        self.writer.write_goto(end_label)
        self.writer.write_label(if_label)
        self.expect_symbol("{")
        self.compile_statements()
        self.expect_symbol("}")
        self.writer.write_goto(start_label)
        self.writer.write_label(end_label)

    def compile_return(self) -> None:
        """Compiles a return statement."""

        if not (
            self.tokenizer.next_token_type() == cons.SYMBOL
            and self.tokenizer.next_token_val() == ";"
        ):

            self.expect_keyword("return")
            self.compile_expression()
        else:
            self.expect_keyword("return")
            self.writer.write_push(cons.CONST, 0)

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
            self.tokenizer.token_type() == cons.KEYWORD
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
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() in cons.OP
        ):
            op: cons.OpType = self.tokenizer.symbol()  # type: ignore
            self.tokenizer.advance()

            self.compile_term()

            self.compile_op(op)

    def compile_op(self, op: cons.OpType) -> None:
        self.writer.write_arithmetic(op)

    def compile_unary_op(self, op: cons.UnaryOpType) -> None:
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
        if self.tokenizer.token_type() == cons.INTEGER_CONSTANT:
            self.writer.write_push(cons.CONST, int(self.tokenizer.int_val()))
            self.tokenizer.advance()
        # stringConstant
        elif self.tokenizer.token_type() == cons.STRING_CONSTANT:
            self.writer.write_push_str(self.tokenizer.string_val())
            self.tokenizer.advance()
        # varname|varname[expression]| subroutineCall
        elif self.tokenizer.token_type() == cons.IDENTIFIER:
            # varname[expression]| subroutineCall
            if (
                self.tokenizer.next_token_val()
                and self.tokenizer.next_token_val() in "([."
            ):
                # varname[expression]
                if self.tokenizer.next_token_val() == "[":
                    # TODO:add method to write array
                    arr_naem = self.expect_identifier()
                    arr_segment = self.symble_table.kind_of_as_segment(arr_naem)
                    arr_index = self.symble_table.index_of(arr_naem)

                    self.expect_symbol("[")
                    self.compile_expression()
                    self.expect_symbol("]")
                    self.writer.write_push(arr_segment, arr_index)
                    self.writer.write_arithmetic("+")
                    self.writer.write_pop(cons.POINTER, 1)
                    self.writer.write_push(cons.THAT, 0)
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
        elif self.tokenizer.token_type() == cons.SYMBOL:
            if self.tokenizer.symbol() == "(":  # (expression)
                self.expect_symbol("(")
                self.compile_expression()
                self.expect_symbol(")")
            elif self.tokenizer.symbol() in cons.UNARY_OP:  # unaryOpTerm
                op: cons.UnaryOpType = self.expect_symbol(*cons.UNARY_OP)  # type: ignore
                self.compile_term()
                self.compile_unary_op(op)
            else:
                self.compile_error()
        # KeywordConstant
        elif self.tokenizer.token_type() == cons.KEYWORD:
            constant_keyword = self.expect_keyword(*cons.KYWORDS_CONSTANT)  # type: ignore
            if constant_keyword == "this":
                self.writer.write_push(cons.POINTER, 0)
                return
            self.writer.write_push(
                # for false and null it 0
                cons.CONST,
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
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == ")"
        ):
            return counter

        else:
            self.compile_expression()
            counter += 1

        while (
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == ","
        ):
            self.expect_symbol(",")
            self.compile_expression()
            counter += 1

        return counter

    #  """helper methods:"""

    def expect_type(self, *additional_keywords: str) -> str:
        """return the type, and advence the tokenizer
        type can be either keyword or identifier
        we can add additional keyword (like void),
        additional_keywords must be form keyword"""
        # type is keyword int , boolean or char
        if self.tokenizer.token_type() == cons.KEYWORD:
            return self.expect_keyword(
                *additional_keywords, *cons.BASIC_TYPES_WITH_VOID
            )
        # if type is a class
        elif self.tokenizer.token_type() == cons.IDENTIFIER:
            return self.expect_identifier()
        else:
            raise ValueError("expecte type (kyword or identifier) but is not")

    def compile_subroutineCall(self):

        # subroutineCall(): is mhetod in class
        # ClassName.function(): is function of class
        # varName.method(): is method of object

        base_name: str = self.expect_identifier()

        n_args: int = 0
        if (  # check if is method call
            self.tokenizer.token_type() == cons.SYMBOL
            and self.tokenizer.symbol() == "."
        ):
            self.expect_symbol(".")
            # ClassName.function() | varName.method()
            if self.symble_table.kind_of(base_name):
                # varName.method()
                # if is method call
                # 1. change function name to ClassName.function
                # 2. push object onto stack
                # 3. add 1 to counter arguments
                object_name = base_name
                func_name = (
                    self.symble_table.type_of(object_name)
                    + "."
                    + self.expect_identifier()
                )
                self.writer.write_push(
                    self.symble_table.kind_of_as_segment(object_name),
                    self.symble_table.index_of(object_name),
                )
                n_args += 1
            else:  # ClassName.function()
                func_name = base_name + "." + self.expect_identifier()
        else:
            # subroutineCall()
            func_name = f"{self.curr_class}.{base_name}"
            n_args += 1
            self.writer.write_push(
                cons.POINTER,
                0,
            )
        self.expect_symbol("(")
        n_args += self.compile_expression_list()
        self.expect_symbol(")")

        # write the function
        self.writer.write_call(func_name, n_args)

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

    def expect_keyword(self, *keyword: str) -> cons.KeywordType:
        """
        check that if current token is keyword
        **advance** token and return the keyword

        Args:
            keyword (_type_): *arg that can be the keyword
        """
        if (self.tokenizer.token_type() != cons.KEYWORD) or (
            self.tokenizer.keyword() not in keyword
        ):
            self.compile_error()
        ret: cons.KeywordType = self.tokenizer.keyword()
        self.tokenizer.advance()
        return ret

    def expect_identifier(self) -> str:
        if self.tokenizer.token_type() != cons.IDENTIFIER:
            self.compile_error()
        ret = self.tokenizer.identifier()
        self.tokenizer.advance()
        return ret

    def expect_symbol(self, *symbol: str) -> cons.SymbolsType:

        if (self.tokenizer.token_type() != cons.SYMBOL) or (
            self.tokenizer.symbol() not in symbol
        ):
            self.compile_error()
        ret: cons.SymbolsType = self.tokenizer.symbol()  # type: ignore
        self.tokenizer.advance()
        return ret
