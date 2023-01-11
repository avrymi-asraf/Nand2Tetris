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

ARG: Literal["argunemt"] = "argunemt"
VAR: Literal["var"] = "var"
STATIC: Literal["static"] = "static"
FIELD: Literal["FIELD"] = "FIELD"
CONST: Literal["constant"] = "constant"
LOCAL: Literal["local"] = "local"
THIS: Literal["this"] = "this"
THAT: Literal["that"] = "that"
POINTER: Literal["pointer"] = "pointer"
TEMP: Literal["temp"] = "temp"


CONSTRUCTOR = "constructor"
FUNCTION = "function"
METHOD = "method"

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
UNARY_OP = {"-", "~", "#", "-"}  # TODO WHY - TWICE?
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
STATEMENT_KEYWORDS = ["let", "if", "while", "do", "return"]
KeywordType = Literal[
    "calss",
    "method",
    "function",
    "constructor",
    "int",
    "BOOLEAN",
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
KEYWORDS:set[KeywordType] = {
    "calss",
    "method",
    "function",
    "constructor",
    "int",
    "BOOLEAN",
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

BASIC_TYPES_WITH_VOID = ["int", "char", "boolean", "void"]

opDict = {
    "+": "ADD",
    "-": "SUB",
    "/": "/",  # TODO
    "|": "OR",
    "&": "&",  # TODO
    "=": "EQ",
    "<": "LT",
    ">": "GT",
    "&amp;": "&amp;",  # TODO
    ">>": "SHIFTLEFT",
    "<<": "SHIFRIGHT",
}
segmentsDict: dict[str, str] = {
    VAR: "var",
}
# "NEG",  "AND", , "NOT", #TODO


# Typing
CurrKindType = Literal["argunemt", "var", "static", "FIELD"]


TokenKindType = Literal[
    "keyword",
    "symbol",
    "integerConstant",
    "stringConstant",
    "identifier",
    "op",
]
TokenType = Tuple[TokenKindType, str]
SymbolTableType = Dict[str, Tuple[str, str, int]]
