
ARG = "argunemt"
VAR = "var"
STATIC = "static"
FIELD = "FIELD"
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
UNARY_OP = {"-", "~", "#", "-"} #TODO WHY - TWICE?
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

opDict = {
    "+" : "ADD",
    "-" : "SUB",
    "/" : "/", #TODO
    "|" : "OR", 
    "&": "&", #TODO
    "=" : "EQ", 
    "<" : "LT",
    ">" : "GT",
    "&amp;" : "&amp;", #TODO
    ">>" : "SHIFTLEFT",
    "<<" : "SHIFRIGHT"
}

# "NEG",  "AND", , "NOT", #TODO

           