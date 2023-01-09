
ARG = "ARG"
VAR = "VAR"

STATIC = "STATIC"
FIELD = "FIELD"
CONST = "CONSTANT"

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
BASIC_TYPES = ["int", "char", "boolean"]
BASIC_TYPES_WITH_VOID = ["int", "char", "boolean", "void"]

#TODO FIX
segmentsDict = { STATIC : "static", FIELD : "local",  ARG : "arg", VAR : "local" }