import re


class RegxPatterns():
    re_comments = re.compile(r'(?P<comments>//.*|/\*.*\*/)')
    re_space = re.compile(r'(?P<space>\s+)')
    re_SYMBOL = re.compile(
        r'(?P<SYMBOL>\{|\}|\(|\)|\[|\]|\.|,|;|\+|-|\*|/|&|\||<|>|=|~)')
    re_KEYWORD = re.compile(
        r'(?P<KEYWORD>class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return)')
    re_INT_CONST = re.compile(r'(?P<INT_CONST>\d+)')
    re_STRING_CONST = re.compile(r'(?:(?P<STRING_CONST>\".*?\"|\'.*?\'))')
    re_IDENTIFIER = re.compile(r'(?P<IDENTIFIER>[^0-9 ][\w]*)')
    re_mismatch = re.compile(r'(?P<mismatch>.)')

    re_token = re.compile(
        re_SYMBOL.pattern + "|" +
        re_KEYWORD.pattern + "|" +
        re_INT_CONST.pattern + "|" +
        re_STRING_CONST.pattern + "|" +
        re_IDENTIFIER.pattern + "|" +
        re_space.pattern + "|" +
        re_mismatch.pattern
    )
    re_remove_comments = re.compile(
        re_comments.pattern + "|(?:"+re_STRING_CONST.pattern + ")")

    re_class_name = re_IDENTIFIER
    re_subroutinDoc = re_IDENTIFIER
    re_varName = re_IDENTIFIER
    re_type = re.compile(
        r'(?P<type>int|char|boolean|'+re_class_name.pattern+')')

    re_classVerDoc = re.compile(r"(?P<classVerDoc>(static|field)" + re_type.pattern +
                                "\{" + re_varName.pattern + "\(,"+re_varName.pattern + '\)*;)')
    re_class = re.compile(r"(?P<re_class>class" + re_class_name.pattern +
                          "\{" + re_classVerDoc.pattern + "*"+re_subroutinDoc.pattern + "*" + "\})")
