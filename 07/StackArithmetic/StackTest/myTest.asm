
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
@Yltz.1
D;JLT            
@SP       
A = M-1
D = M
@true.1 
D;JLT          
(sub.1)  
@SP
A = M
D = D-M
@false.1
D;JGE
@true.1
0;JMP
(Yltz.1)
@SP
A = M-1
D = M
@false.1
D;JGE
@sub.1
0;JMP

(true.1)
@SP
A = M-1
M = -1
@end.1
0;JMP

(false.1)
@SP
A = M-1
M = 0

(end.1) 
