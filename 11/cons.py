from telnetlib import SE
from typing import (
    Dict,
    Literal,
    Set,
    Tuple,
)

ARG = "arg"
VAR = "var"
STATIC = "static"
FIELD = "field"

VarKindType = Literal["static", "field", "arg", "var"]
VARKINDS: Set[VarKindType] = {"static", "field", "arg", "var"}


CONST = "constant"
LOCAL = "local"
THIS = "this"
THAT = "that"
POINTER = "pointer"
TEMP = "temp"

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
SEGMENTS: Set[SegmentType] = {
    "pointer",
    "static",
    "temp",
    "constant",
    "argument",
    "this",
    "that",
    "local",
}

kind_to_segment: Dict[str, SegmentType] = {
    "arg": "argument",
    "var": "local",
    "static": "static",
    "field": "this",
    "pointer": "pointer",
}


CONSTRUCTOR = "constructor"
FUNCTION = "function"
METHOD = "method"

FunctionType = Literal[
    "method",
    "function",
    "constructor",
]
FUNCTIONS: Set[FunctionType] = {
    "method",
    "function",
    "constructor",
}


KEYWORD = "keyword"
SYMBOL = "symbol"
IDENTIFIER = "identifier"
VARNAME = IDENTIFIER
INTEGER_CONSTANT = "integerConstant"
STRING_CONSTANT = "stringConstant"
TokenKindType = Literal[
    "keyword",
    "symbol",
    "integerConstant",
    "stringConstant",
    "identifier",
]

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
SYMBOLS: Set[SymbolsType] = {
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
OP: Set[OpType] = {
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
    "/": "call Math.divide 2",  # TODO
    "|": "or",
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
    "*": "call Math.multiply 2",
}

UnaryOpType = Literal["-", "~", "#", "-"]
UNARY_OP: Set[UnaryOpType] = {"-", "~", "#"}  # TODO WHY - TWICE?

STATEMENT_KEYWORDS = ["let", "if", "while", "do", "return"]
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
KEYWORDS: Set[KeywordType] = {
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

BASIC_TYPES = {"int", "char", "boolean"}
BASIC_TYPES_WITH_VOID = {"int", "char", "boolean", "void"}

# Typing

TokenType = Tuple[TokenKindType, str]
SymbolTableType = Dict[str, Tuple[str, VarKindType, int]]
