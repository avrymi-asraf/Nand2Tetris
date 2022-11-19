
# push segment index
push =  """@index
D = A
@SP
A = M
M = D

@SP
M =M+1"""


#pop segment index

pop =  """

@SP
A = M
D = M

@data
M = D

@index
D = A

@segment 
D = D + A

@D
M = data
"""

add = """
@SP
A=M
D=M

@SP 
AM = M-1
M = D+M

@SP
M =M+1"""

sub = """
@SP
A=M
D=M

@SP 
AM = M-1
M = M-D

@SP
M =M+1"""




