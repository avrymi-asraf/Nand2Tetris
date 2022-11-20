
class Codes:
    #TODO delete lines

    push_constant =  """
//**push constant**
@index
D = A

@SP
A = M
M = D

@SP
M = M+1"""

    push_argument =  """
//**push argument**
//go to segment at index

@segment
D = M

@index
D = D+A

A = D
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1"""

    push_static = """
//**push static**
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
//**pop argument**

//find address
@segment
D = M

@index
D = D+A

@_temp_index
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_index
M = D

//decrement SP
@SP
M = M-1

"""

    pop_static = """ 
//**pop static**

//take data from top of stack
@SP
A = M 

A = A-1
D = M

//write data inside segment at the given index
@index
M = D

//decrement SP
@SP
M = M-1

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

@eq._counter
D;JEQ

//if is not equal 
@0
D = A
@SP
A = M-1
M = D

@end._counter
0;JMP

(eq._counter)
    @1
    D = -A
    @SP
    A = M-1
    M = D


(end._counter)
"""  
  
    C_lt = """
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz._counter       
D;JLT
//else
@SP     
A = M-1
D = M
@false._counter      // if second argument < 0  
D;JLT 
            //else sub them
@subthem._counter
0;JMP

(tltz._counter)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @true._counter
    D;JGT
    //else sub them       
    @subthem._counter    
    0;JMP
(subthem._counter)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @true._counter
    D;JGE 
    //else false
    @false._counter
    0;JMP   
(true._counter)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end._counter
    0;JMP
(false._counter)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end._counter)
""" 
    
    C_gt = """
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz._counter       
D;JLT
//else
@SP     
A = M-1
D = M
@true._counter      // if second argument < 0  
D;JLT 
            //else sub them
@subthem._counter
0;JMP

(tltz._counter)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @false._counter
    D;JGT
    //else sub them       
    @subthem._counter    
    0;JMP
(subthem._counter)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @false._counter
    D;JGE 
    //else true
    @true._counter
    0;JMP   
(true._counter)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end._counter
    0;JMP
(false._counter)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end._counter) 
"""
    
    C_and = """
@SP
AM = M-1
D = M

@SP
A = M-1
M = D&M
"""
    
    C_or= """
//OR  
@SP
AM = M-1
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




    # "SCREEN":"16384",
    #         "KBD":"24576",
    #         "SP":"0",
    #         "LCL":"1",
    #         "ARG":"2",
    #         "THIS":"3",
    #         "THAT":"4"