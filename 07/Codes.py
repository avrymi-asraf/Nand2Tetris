
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

    pop_argument = """
//push
@segment
D = M
@index
D=D+A
//
@_temp_index
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
@SP
AM = M-1
D = M

A = A-1
D = D-M

@eq
D;JEQ

//if is not equal 
@0
D = A
@SP
A = M-1
M = D

@end
0;JMP

(eq)
    @-1
    D = A
    @SP
    A = M-1
    M = D


(end)
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

    C_shiftleft = """
     """

    C_shiftright = """
     """
