
class Codes:

    push_constant =  """
//push
@index
D = A
@SP
A = M
M = D

@SP
M = M+1"""

    push_argument =  """
//go to segment at index

@segment
D = M

@index
D=D+A

@D
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1"""


    push_static = """
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@index
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1"""


    pop_argument = """ 
//find segment at index
@segment
D = M

@index
D=D+A

@_temp_index
M = D

//take data from top of stack
@SP
A = M
D = M

//write data inside segment at the given index
@_temp_index
M = D

//decrement SP
@SP
M =M-1

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
    @1
    D = -A
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


