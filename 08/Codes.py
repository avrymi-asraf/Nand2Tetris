
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

    push_segment =  """
//**push segment**


@_segment
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M + 1
"""

    push_new_label = """  
@_label
D = A

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1
"""

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
A = M -1
D = M

//write data inside segment at the given index
@index
M = D

//decrement SP
@SP
M = M-1

"""

    C_add = """
//**add**
@SP
AM=M-1
D=M

@SP 
AM = M-1
M = D+M

@SP
M =M+1"""

    C_sub = """
//**sub**
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
@Yltz._counter
D;JLT            
@SP       
A = M-1
D = M
@true._counter 
D;JLT          
(sub._counter)  
@SP
A = M
D = D-M
@false._counter
D;JGE
@true._counter
0;JMP
(Yltz._counter)
@SP
A = M-1
D = M
@false._counter
D;JGE
@sub._counter
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
@Yltz._counter
D;JLT            
@SP       
A = M-1
D = M
@false._counter 
D;JLT          
(sub._counter)  
@SP
A = M
D = D-M
@true._counter
D;JGT
@false._counter
0;JMP
(Yltz._counter)
@SP
A = M-1
D = M
@true._counter
D;JGE
@sub._counter
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
//**not**
@SP
A = M-1
M = !M
    """

    C_shiftleft = """
//**C_shiftleft**
@SP
A = M-1
M = M<<
"""

    C_shiftright = """
//**C_shiftright**
@SP
A = M-1
M = M>>
"""

    push_this_that ="""
//**push this that**
@index
D = M

@SP         
A=M
M = D

@SP
M=M+1
    """

    pop_this_that ="""
//**pop this that**
@SP
A = M-1      
D = M

@index
M = D

@SP
M = M-1
"""


    pop_temp = """ 
//**pop temp**
@SP
A = M-1      
D = M

@Rnew_index
M = D

@SP
M = M-1      

    """
    
    push_temp ="""
//**push temp**
@Rnew_index
D = M

@SP
A = M     
M = D

@SP
M = M+1 

    """

    C_goto = """
//**goto**
@_label
0;JMP
"""

    C_if = """
//**if**
@SP
AM = M-1
D = M

@_label
D;JLT
D;JGT
"""

C_reposition = """ 
@_source
D = M

@_source_ind
D = D + A

@_dest
M = D
"""