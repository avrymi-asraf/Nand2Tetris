
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
@SP
A = M-1
M = -M
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
@SP 
MA = M-1
D = M
// if first argument < 0
@tltz       
D;JLT
//else
@SP     
A = A-1
D = M
@false      // if second argument < 0  
D;JLT 
            //else sub them
@subthem
0;JMP

(tltz)
    @SP
    A = A-1
    D = M
    // if second argument >0
    @true
    D;JGT
    //else sub them       
    @subthem    
    0;JMP
(subthem)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @true
    D;JGE 
    //else false
    @false
    0;JMP   
(true)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end
    0;JMP
(false)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end)
""" 
    
    C_gt = """
@SP 
MA = M-1
D = M
// if first argument < 0
@tltz       
D;JLT
//else
@SP     
A = A-1
D = M
@true      // if second argument < 0  
D;JLT 
            //else sub them
@subthem
0;JMP

(tltz)
    @SP
    A = A-1
    D = M
    // if second argument >0
    @false
    D;JGT
    //else sub them       
    @subthem    
    0;JMP
(subthem)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @false
    D;JGE 
    //else true
    @true
    0;JMP   
(true)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end
    0;JMP
(false)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end) 
"""
    
    C_and = """
@SP
MA = M-1
D = M

@SP
A = M-1
M = D&M
"""
    
    C_or= """
//OR  
@SP
MA = M-1
D = M

@SP
A = M-1
M = D|M
    """
   
    C_not = """
@SP
A = M-1
M = !M
    """

    C_shiftleft = """
@SP
A = M-1
M = M<<
"""

    C_shiftright = """
@SP
A = M-1
M = M>>
"""


