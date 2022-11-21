
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

    push_segment =  """
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

    pop_segment = """ 
//**pop argument**

//find address
@segment
D = M

@index
D = D + A

@_temp_index
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_index
A = M
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
D = M   //old value
A = A-1
D = D-M // the difference
@eq._counter
D;JEQ       //if is not equal         
@SP          //else
A = M-1
M = 0
@end._counter
0;JMP
(eq._counter) //set to true  
    @SP
    A = M-1
    M = -1
(end._counter)
"""  
  
    C_lt = """
@SP 
AM = M-1
D = M
@tltz._counter  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false._counter   // if second argument < 0  
D;JLT 
@subthem._counter //else sub them
0;JMP
(tltz._counter)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true._counter  // if second argument >= 0
    D;JGE     
    @subthem._counter  //else sub them  
    0;JMP
(subthem._counter)
    @SP
    A = M 
    D = M-D     //second argument - first argument
    @true._counter  
    D;JGT
    @false._counter //else false
    0;JMP   
(true._counter)
    @SP
    A = M-1
    M = -1    
    @end._counter
    0;JMP
(false._counter)
    @SP
    A = M-1
    M = 0
(end._counter)
""" 
    
    C_gt = """
@SP 
AM = M-1
D = M
@tltz._counter   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true._counter      // if second argument < 0  
D;JLT 
@subthem._counter   //else sub them
0;JMP
(tltz._counter)
    @SP
    A = M -1
    D = M
    @false._counter // if second argument >0
    D;JGT      
    @subthem._counter    //else sub them 
    0;JMP
(subthem._counter)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false._counter
    D;JGE 
    @true._counter //else true
    0;JMP   
(true._counter)
    @SP
    A = M-1
    M = -1   
    @end._counter
    0;JMP
(false._counter)
    @SP
    A = M-1
    M = 0
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

    push_this_that ="""

"@index
D = M

@SP         
A=M
M = D

@SP
M=M+1"
    """

    pop_this_that ="""

@SP
A = M-1      
D = M

@index
M = D

@SP
M = M-1
"""

AM=M-1      
D=M     //data from stack
@R13
A=M     //
M=D
    """
    pop_temp = """ 
@R5  
D=M
@index 
D=D+A    
@R13      
M=D         
@SP
AM=M-1      
D=M     
A=M     
M=D
    """
    push_temp ="""
@R5  
D=M
@index
A=D+A    
D=M      
@SP         
A=M
M=D
@SP
M=M+1
    """
