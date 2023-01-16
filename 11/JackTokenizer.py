"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
from typing import (
    Generator,
    Iterator,
    List,
    Tuple,
    TextIO,
    Optional,
    Dict,
    Union,
)
import cons
from regex import RegxPatterns

KINDS = (
    "field",
    "var",
)


class JackTokenizer:
    """Removes all comments from the input stream and breaks it
    into Jack language tokens, as specified by the Jack grammar.

    ## Lexical Elements

    The Jack language includes five types of terminal elements (tokens).

    - keyword: 'class' | 'constructor' | 'function' | 'method' | 'field' |
               'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' |
               'false' | 'null' | 'this' | 'let' | 'do' | 'if' | 'else' |
               'while' | 'return'
    - symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' |
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
    - integerConstant: A decimal number in the range 0-32767.
    - StringConstant: '"' A sequence of Unicode characters not including
                      double quote or newline '"'
    - identifier: A sequence of letters, digits, and underscore ('_') not
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.

    - op: '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
    - unaryOp: '-' | '~' | '^' | '#'
    - keywordConstant: 'true' | 'false' | 'null' | 'this'

    Note that ^, # correspond to shiftleft and shiftright, respectively.
    """

    def __init__(self, input_stream: TextIO) -> None:
        """Opens the input stream and gets ready to tokenize it.

        Args:
            input_stream (typing.TextIO): input stream.
        """
        self.tokens_text: str
        self.tokens_list: List[cons.TokenType]
        self.curr_token: cons.TokenType

        self.tokens_text = input_stream.read()
        # remove comments
        self.tokens_text = RegxPatterns.re_remove_comments.sub(
            r"\g<stringConstant>", self.tokens_text
        )
        # remove whitespace and newlines
        self.tokens_text = RegxPatterns.re_space.sub(
            " ", self.tokens_text
        )

        self.__create_token_list()

    def __token_error(self, mst=""):
        """## raise value error
        ### format error message:
        `Invalid token:try print _mst_ but current command is _curr_token[0]_`

        """
        return ValueError(
            "Invalid token:try print {} but current command is {}".format(
                mst, self.curr_token[0]
            )
        )

    def __create_token_list(self) -> None:
        """
        Create list with all tokens, using iter_tokens
        """
        iter_token = self.iter_tokens()
        self.tokens_list = [token for token in iter_token]
        self.advance()

    def has_more_tokens(self) -> bool:
        """Do we have more tokens in the input?

        Returns:
            bool: True if there are more tokens, False otherwise.
        """
        return len(self.tokens_list) > 0

    def advance(self) -> None:
        """Gets the next token from the input and makes it the current token.
        This method should be called if has_more_tokens() is true.
        Initially there is no current token.
        """
        if self.has_more_tokens():
            self.curr_token = self.tokens_list.pop(0)

    def token_type(self) -> str:
        """
        Returns:
            str: the type of the current token, can be
            "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        #"""

        return self.curr_token[0]

    def keyword(self) -> cons.KeywordType:
        """
        Returns:
            str: the keyword which is the current token.
            Should be called only when token_type() is "keyword".
            Can return "CLASS", "METHOD", "FUNCTION", "CONSTRUCTOR", "INT",
            "BOOLEAN", "CHAR", "VOID", "VAR", "STATIC", "FIELD", "LET", "DO",
            "IF", "ELSE", "WHILE", "RETURN", "TRUE", "FALSE", "NULL", "THIS"
        """
        if self.curr_token[0] == "keyword":
            return self.curr_token[1]  # type: ignore
        else:
            raise self.__token_error("keyword")

    def symbol(self) -> str:
        """
        Returns:
            str: the character which is the current token.
            Should be called only when token_type() is "symbol".
            Recall that symbol was defined in the grammar like so:
            symbol: '{' | '}' | '(' | ')' | '[' | ']' | '.' | ',' | ';' | '+' |
              '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~' | '^' | '#'
        """
        if self.curr_token[0] == "symbol":
            return self.curr_token[1]
        else:
            raise self.__token_error("symbol")

    def identifier(self) -> str:
        """
        Returns:
            str: the identifier which is the current token.
            Should be called only when token_type() is "identifier".
            Recall that identifiers were defined in the grammar like so:
            identifier: A sequence of letters, digits, and underscore ('_') not
                  starting with a digit. You can assume keywords cannot be
                  identifiers, so 'self' cannot be an identifier, etc'.
        """
        if self.curr_token[0] == "identifier":
            return self.curr_token[1]
        else:
            raise self.__token_error("identifier")

    def int_val(self) -> str:
        """
        Returns:
            str: the integer value of the current token.
            Should be called only when token_type() is "integerConstant".
            Recall that integerConstant was defined in the grammar like so:
            integerConstant: A decimal number in the range 0-32767.
        """
        if self.curr_token[0] == "integerConstant":
            return self.curr_token[1]
        else:
            raise self.__token_error("integerConstant")

    def string_val(self) -> str:
        """
        Returns:
            str: the string value of the current token, without the double
            quotes. Should be called only when token_type() is "stringConstant".
            Recall that StringConstant was defined in the grammar like so:
            StringConstant: '"' A sequence of Unicode characters not including
                      double quote or newline '"'
        """
        if self.curr_token[0] == "stringConstant":
            return self.curr_token[1]
        else:
            raise self.__token_error("stringConstant")

    def iter_tokens(
        self,
    ) -> Generator[cons.TokenType, None, None]:
        """Iterate over tokens
        Returns:(token_type, token_value)
        """
        replacement = {"<": "&lt;", ">": "&gt;", "&": "&amp;"}
        for token in RegxPatterns.re_token.finditer(self.tokens_text):
            if token.lastgroup == "space":
                continue
            elif (
                token.lastgroup == "symbol" and token.group() in "<>&"
            ):
                yield (token.lastgroup, replacement[token.group()])
            elif token.lastgroup == "stringConstant":
                yield (
                    token.lastgroup,
                    token.group().replace('"', ""),
                )
            elif token.lastgroup == "keyword":
                yield (
                    token.lastgroup,
                    token.group().replace(" ", ""),
                )
            else:
                yield (token.lastgroup, token.group())  # type: ignore

    def next_token_val(self) -> str:
        if self.has_more_tokens():
            return self.tokens_list[0][1]
        raise Exception("next_token_val not exists")

    def next_token_type(self) -> cons.TokenKindType:
        if self.has_more_tokens():
            return self.tokens_list[0][0]
        raise Exception("next_token_type not exists")
