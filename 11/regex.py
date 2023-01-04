import re


class RegxPatterns:
    re_comments = re.compile(r"(?P<comments>//.*|/\*(.|\n)*?\*/)")
    re_space = re.compile(r"(?P<space>\s+|\n)")
    re_symbol = re.compile(
        r"(?P<symbol>\{|\}|\(|\)|\[|\]|\.|,|;|\+|-|\*|/|&|\||<|>|=|~)"
    )
    re_keyword = re.compile(
        r"(?P<keyword>class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return)(?![\w])"
    )
    re_integerConstant = re.compile(r"(?P<integerConstant>\d+)")
    re_stringConstant = re.compile(
        r"(?:(?P<stringConstant>\".*?\"|\'.*?\'))"
    )
    re_identifier = re.compile(r"(?P<identifier>[^0-9 ][\w]*)")
    re_mismatch = re.compile(r"(?P<mismatch>.)")

    re_token = re.compile(
        re_symbol.pattern
        + "|"
        + re_keyword.pattern
        + "|"
        + re_integerConstant.pattern
        + "|"
        + re_stringConstant.pattern
        + "|"
        + re_identifier.pattern
        + "|"
        + re_space.pattern
        + "|"
        + re_mismatch.pattern
    )
    re_remove_comments = re.compile(
        re_comments.pattern + "|" + re_stringConstant.pattern
    )


