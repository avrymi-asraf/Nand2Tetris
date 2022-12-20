import re

code_example_comments = """
var String message; // this is my comment
var String message; /* this is my comment */
let message = "The //message"  //this is my comment
ver String str3;   /*This is a Comments*/
let str3 = "http://google.com"
ver String str4;  //Comments
let str4 = "('file:///xghsghsh.html/')"
ver String str5;  //comments
let str5 = "{\"temperature\": {\"type\"}}
"""



re_comments = re.compile(r"(?P<commant>//.*|/\*.*\*/)|(?:(?P<String>\".*\"))")
tokens = re_comments.finditer(code_example_comments)
for token in tokens:
    print (token.groupdict())

