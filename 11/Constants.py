from ast import UnaryOp
from typing import (
    Callable,
    Dict,
    Literal,
    Set,
    List,
    TextIO,
    Tuple,
    Optional,
    Union,
)

from sympy import Segment

ARG = "argument"
VAR = "var"
STATIC = "static"
FIELD = "field"
CONST = "constant"
LOCAL = "local"
THIS = "this"
THAT = "that"
POINTER = "pointer"
TEMP = "temp"


CONSTRUCTOR = "constructor"
FUNCTION = "function"
METHOD = "method"

KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
VARNAME = IDENTIFIER
INTEGER_CONSTANT = "integerConstant"
STRING_CONSTANT = "stringConstant"
KYWORDS_CONSTANT = {"true", "false", "null", "this"}
SymbolsType = Literal[
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
]
SYMBOLS: set[SymbolsType] = {
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
OpType = Literal[
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
    "un-",
    "un~",
    "un#",
]
OP: set[OpType] = {
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
    "un-",
    "un~",
    "un#",
}
opDict = {
    "+": "add",
    "-": "sub",
    "/": "/",  # TODO
    "|": "OR",
    "&": "&",  # TODO
    "=": "eq",
    "&lt;": "lt",
    "&gt;": "gt",
    "&amp;": "and",  # TODO
    ">>": "SHIFTLEFT",
    "<<": "SHIFRIGHT",
    "un-": "neg",
    "un~": "not",
    "un#": "shiftright",
}

UnaryOpType = Literal["-", "~", "#", "-"]
UNARY_OP: set[UnaryOpType] = {"-", "~", "#"}  # TODO WHY - TWICE?
un_op_dict: dict[UnaryOpType, str] = {
    "-": "neg",
    "~": "not",
    "#": "shiftright",
}
STATEMENT_KEYWORDS = ["let", "if", "while", "do", "return"]
VarKindType = Literal["static", "field", "arg", "var"]
VARKINDS: set[VarKindType] = {"static", "field", "arg", "var"}
KeywordType = Literal[
    "calss",
    "method",
    "function",
    "constructor",
    "int",
    "boolean",
    "char",
    "void",
    "var",
    "static",
    "FIELD",
    "let",
    "do",
    "if",
    "else",
    "while",
    "return",
    "true",
    "false",
    "null",
    "this",
]
KEYWORDS: set[KeywordType] = {
    "calss",
    "method",
    "function",
    "constructor",
    "int",
    "boolean",
    "char",
    "void",
    "var",
    "static",
    "FIELD",
    "let",
    "do",
    "if",
    "else",
    "while",
    "return",
    "true",
    "false",
    "null",
    "this",
}
FunctionType = Literal[
    "method",
    "function",
    "constructor",
]
FUNCTIONS: set[FunctionType] = {
    "method",
    "function",
    "constructor",
}

SegmentType = Literal[
    "pointer",
    "static",
    "temp",
    "constant",
    "argument",
    "this",
    "that",
    "local",
]
SEGMENTS: set[SegmentType] = {
    "pointer",
    "static",
    "temp",
    "constant",
    "argument",
    "this",
    "that",
    "local",
}
BASIC_TYPES = {"int", "char", "boolean"}

BASIC_TYPES_WITH_VOID = {"int", "char", "boolean", "void"}

segmentsDict: dict[str, str] = {
    VAR: "var",
}
# "NEG",  "AND", , "NOT", #TODO


# Typing
CurrKindType = Literal["argunemt", "var", "static", "field"]


TokenKindType = Literal[
    "keyword",
    "symbol",
    "integerConstant",
    "stringConstant",
    "identifier",
    "op",
]
TokenType = Tuple[TokenKindType, str]
SymbolTableType = Dict[str, Tuple[str, VarKindType, int]]
