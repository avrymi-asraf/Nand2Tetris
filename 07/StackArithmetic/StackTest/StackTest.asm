
//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP
AM = M-1
D = M

A = A-1
D = D-M

@eq.1
D;JEQ

//if is not equal 
@0
D = A
@SP
A = M-1
M = D

@end.1
0;JMP

(eq.1)
    @1
    D = -A
    @SP
    A = M-1
    M = D


(end.1)

//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@16
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP
AM = M-1
D = M

A = A-1
D = D-M

@eq.2
D;JEQ

//if is not equal 
@0
D = A
@SP
A = M-1
M = D

@end.2
0;JMP

(eq.2)
    @1
    D = -A
    @SP
    A = M-1
    M = D


(end.2)

//**push constant**
@16
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP
AM = M-1
D = M

A = A-1
D = D-M

@eq.3
D;JEQ

//if is not equal 
@0
D = A
@SP
A = M-1
M = D

@end.3
0;JMP

(eq.3)
    @1
    D = -A
    @SP
    A = M-1
    M = D


(end.3)

//**push constant**
@892
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz.4       
D;JLT
//else
@SP     
A = M-1
D = M
@false.4      // if second argument < 0  
D;JLT 
            //else sub them
@subthem.4
0;JMP

(tltz.4)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @true.4
    D;JGT
    //else sub them       
    @subthem.4    
    0;JMP
(subthem.4)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @true.4
    D;JGE 
    //else false
    @false.4
    0;JMP   
(true.4)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end.4
    0;JMP
(false.4)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end.4)

//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@892
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz.5       
D;JLT
//else
@SP     
A = M-1
D = M
@false.5      // if second argument < 0  
D;JLT 
            //else sub them
@subthem.5
0;JMP

(tltz.5)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @true.5
    D;JGT
    //else sub them       
    @subthem.5    
    0;JMP
(subthem.5)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @true.5
    D;JGE 
    //else false
    @false.5
    0;JMP   
(true.5)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end.5
    0;JMP
(false.5)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end.5)

//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz.6       
D;JLT
//else
@SP     
A = M-1
D = M
@false.6      // if second argument < 0  
D;JLT 
            //else sub them
@subthem.6
0;JMP

(tltz.6)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @true.6
    D;JGT
    //else sub them       
    @subthem.6    
    0;JMP
(subthem.6)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @true.6
    D;JGE 
    //else false
    @false.6
    0;JMP   
(true.6)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end.6
    0;JMP
(false.6)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end.6)

//**push constant**
@32767
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz.7       
D;JLT
//else
@SP     
A = M-1
D = M
@true.7      // if second argument < 0  
D;JLT 
            //else sub them
@subthem.7
0;JMP

(tltz.7)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @false.7
    D;JGT
    //else sub them       
    @subthem.7    
    0;JMP
(subthem.7)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @false.7
    D;JGE 
    //else true
    @true.7
    0;JMP   
(true.7)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end.7
    0;JMP
(false.7)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end.7) 

//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@32767
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz.8       
D;JLT
//else
@SP     
A = M-1
D = M
@true.8      // if second argument < 0  
D;JLT 
            //else sub them
@subthem.8
0;JMP

(tltz.8)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @false.8
    D;JGT
    //else sub them       
    @subthem.8    
    0;JMP
(subthem.8)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @false.8
    D;JGE 
    //else true
    @true.8
    0;JMP   
(true.8)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end.8
    0;JMP
(false.8)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end.8) 

//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
// if first argument < 0
@tltz.9       
D;JLT
//else
@SP     
A = M-1
D = M
@true.9      // if second argument < 0  
D;JLT 
            //else sub them
@subthem.9
0;JMP

(tltz.9)
    @SP
    A = M-1
    D = M
    // if second argument >0
    @false.9
    D;JGT
    //else sub them       
    @subthem.9    
    0;JMP
(subthem.9)
    @SP
    A = M
    D = D-M //D second argument, M first argument
    @false.9
    D;JGE 
    //else true
    @true.9
    0;JMP   
(true.9)
    @1
    D = -A
    @SP
    A = M-1
    M = D    
    @end.9
    0;JMP
(false.9)
    @0
    D = A
    @SP
    A = M-1
    M = D
(end.9) 

//**push constant**
@57
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@31
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@53
D = A

@SP
A = M
M = D

@SP
M = M+1
//add
@SP
AM=M-1
D=M

@SP 
AM = M-1
M = D+M

@SP
M =M+1
//**push constant**
@112
D = A

@SP
A = M
M = D

@SP
M = M+1
//add
@SP
AM=M-1
D=M

@SP 
AM = M-1
M = M-D

@SP
M =M+1 
@SP
A = M-1
M = -M

@SP
AM = M-1
D = M

@SP
A = M-1
M = D&M

//**push constant**
@82
D = A

@SP
A = M
M = D

@SP
M = M+1
//OR  
@SP
AM = M-1
D = M

@SP
A = M-1
M = D|M
    
@SP
A = M-1
M = !M
    