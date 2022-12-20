
class Codes:

    push_constant =  """//**push constant**
@_index
D = A

@SP
A = M
M = D

@SP
M = M+1"""

    push_static = """//**push static**
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@_index
D = M
@SP
A = M
M = D
@SP
M = M+1"""

    push_segment =  """//**push segment**
//go to segment at _index
@_segment
D = M

@_index
A = D + A
D = M

//write in SP
@SP
A = M
M = D

//inc SP
@SP
M = M+1"""


    push_segment_adress =  """//**push segment adress**
@_segment
D = M

//write in SP
@SP
A = M
M = D

//inc SP
@SP
M = M + 1
"""

    push_new_label = """//**push_new_label**  
@_label
D = A

//write in SP
@SP
A = M
M = D

//inc SP
@SP
M = M+1
"""

    pop_segment = """//**pop argument**
//find address
@_segment
D = M

@_index
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

    pop_static = """//**pop static**
//take data from top of stack
@SP
A = M -1
D = M

//write data inside segment at the given _index
@_index
M = D

//decrement SP
@SP
M = M-1

"""

    C_add = """//**add**
@SP
AM = M-1
D = M
A = A-1
M = M + D
"""

    C_sub = """//**sub**
@SP
AM=M-1
D=M
A = A-1
M = M-D
"""

    C_neg = """//**neg**
@SP
A = M-1
M = -M
"""
   
    C_eq = """//**eq**
@SP
AM = M-1
D = M   //old value
A = A-1
D = D-M //the difference 
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
  
    C_lt = """//**lt**
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
    
    C_gt = """//**gt**
//**C_gt**
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
    
    C_and = """//**and**
@SP
AM = M-1
D = M
A = A-1
M = D&M
"""
    
    C_or = """//**or**  
@SP
AM = M-1
D = M
A = A-1
M = D|M
    """
   
    C_not = """//**not**
@SP
A = M-1
M = !M
    """

    C_shiftleft = """//**shiftleft**
@SP
A = M-1
M = M<<
"""

    C_shiftright = """//**shiftright**
@SP
A = M-1
M = M>>
"""

    push_this_that ="""//**push this that**
@_index
D = M

@SP         
A=M
M = D

@SP
M=M+1
    """

    pop_this_that ="""//**pop this that**
@SP
A = M-1      
D = M

@_index
M = D

@SP
M = M-1
"""

    pop_temp = """//**pop temp**
@SP
A = M-1      
D = M

@R_new_index
M = D

@SP
M = M-1      
    """
    
    push_temp = """//**push temp**
@R_new_index
D = M

@SP
A = M     
M = D

@SP
M = M+1 
    """

    C_goto = """//**goto**
@_label
0;JMP
"""

    C_if = """//**if**
@SP
AM = M-1
D = M

@_label
D;JNE
"""


    C_reposition_neg_ind = """//**reposition** 
@_source
D = M

@_source_ind_to_reduce
D = D - A

@_dest
M = D
"""

    C_reposition_pos_ind = """//**reposition** 
@_source
D = M

@_source_ind_to_add
D = D + A

@_dest
M = D
"""

    C_updte_address_from_data_neg = """//**updte_address_from_data_neg** 
@_source
D = M

@_source_ind_to_reduce
A = D - A
D = M

@_dest
M = D
"""

    C_pop_to_arg = """//**C_pop_to_arg**
@SP
A = M-1  
D = M

@ARG
A = M
M = D

@SP
M = M-1 
"""

    C_init_sp_to_256 = """//**init**
@256
D = A

@SP
M = D
"""

    C_write_label = """// ** write label
(_label)
"""
