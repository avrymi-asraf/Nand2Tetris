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



re_comments = re.compile(r"//.*|/\*.*\*/|(?:(\".*\"))")
# print(re_comments.sub(r'\1',code_example_comments))



is_number = re.compile(r'(4)')
mo = is_number.search('My number is 433-555-4242.')
print(mo.groups(3))

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
# print(re.sub(re_comments, r'\1', code_example_comments))

