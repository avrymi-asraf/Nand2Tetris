
class Codes:
    push_constant =  """
//push
@index
D = A
@SP
A = M
M = D

@SP
M =M+1"""

    push_argument = """
//push
@segment
D = M
@index
D=D+A
//
@_index
M = D

@SP
A = M
D = M
@_temp_index
A = M
M = D

@SP
M =M-1"""

    C_pop =  """
//pop
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

    C_add = """
//add
@SP
AM=M-1
D=M

@SP 
AM = M-1
M = D+M

@SP
M =M+1"""

    C_sub = """
//add
@SP
AM=M-1
D=M

@SP 
AM = M-1
M = M-D

@SP
M =M+1"""

    C_neg = """ 

    """
    C_eq = """
    """ 
    C_lt = """
    """ 
    C_gt = """ """
    
    C_and = """
    """
    C_or= """
    """
    C_not = """
    """



