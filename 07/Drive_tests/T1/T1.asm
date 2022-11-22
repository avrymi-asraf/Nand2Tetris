
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
D = M   //old value
A = A-1
D = D-M // the difference
@eq.1
D;JEQ       //if is not equal         
@SP          //else
A = M-1
M = 0
@end.1
0;JMP
(eq.1) //set to true  
    @SP
    A = M-1
    M = -1
(end.1)

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
@Yltz.2
D;JLT            
@SP       
A = M-1
D = M
@true.2 
D;JLT          
(sub.2)  
@SP
A = M
D = D-M
@false.2
D;JGE
@true.2
0;JMP
(Yltz.2)
@SP
A = M-1
D = M
@false.2
D;JGE
@sub.2
0;JMP

(true.2)
@SP
A = M-1
M = -1
@end.2
0;JMP

(false.2)
@SP
A = M-1
M = 0

(end.2) 

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
@Yltz.3
D;JLT            
@SP       
A = M-1
D = M
@false.3 
D;JLT          
(sub.3)  
@SP
A = M
D = D-M
@true.3
D;JGT
@false.3
0;JMP
(Yltz.3)
@SP
A = M-1
D = M
@true.3
D;JGE
@sub.3
0;JMP

(true.3)
@SP
A = M-1
M = -1
@end.3
0;JMP

(false.3)
@SP
A = M-1
M = 0

(end.3) 

//**push constant**
@56
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
//**add**
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
    