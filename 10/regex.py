import re


class RegxPatterns():
    re_comments = re.compile(r'(?P<comments>//.*|/\*(.|\n)*?\*/)')
    re_space = re.compile(r'(?P<space>\s+)')
    re_symbol = re.compile(
        r'(?P<symbol>\{|\}|\(|\)|\[|\]|\.|,|;|\+|-|\*|/|&|\||<|>|=|~)')
    re_keyword = re.compile(
        r'(?P<keyword>class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|else|while|return)')
    re_integerConstant = re.compile(r'(?P<integerConstant>\d+)')
    re_stringConstant = re.compile(r'(?:(?P<stringConstant>\".*?\"|\'.*?\'))')
    re_identifier = re.compile(r'(?P<identifier>[^0-9 ][\w]*)')
    re_mismatch = re.compile(r'(?P<mismatch>.)')

    re_token = re.compile(
        re_symbol.pattern + "|" +
        re_keyword.pattern + "|" +
        re_integerConstant.pattern + "|" +
        re_stringConstant.pattern + "|" +
        re_identifier.pattern + "|" +
        re_space.pattern + "|" +
        re_mismatch.pattern
    )
    re_remove_comments = re.compile(
        re_comments.pattern + "|"+re_stringConstant.pattern )

    # re_class_name = re_identifier
    # re_subroutinDoc = re_identifier
    # re_varName = re_identifier
    # re_type = re.compile(
    #     r'(?P<type>int|char|boolean|'+re_class_name.pattern+')')

    # re_classVerDoc = re.compile(r"(?P<classVerDoc>(static|field)" + re_type.pattern +
    #                             "\{" + re_varName.pattern + "\(,"+re_varName.pattern + '\)*;)')
    # re_class = re.compile(r"(?P<re_class>class" + re_class_name.pattern +
    #                       "\{" + re_classVerDoc.pattern + "*"+re_subroutinDoc.pattern + "*" + "\})")
