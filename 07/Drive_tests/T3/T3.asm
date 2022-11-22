
//**push constant**
@32767
D = A

@SP
A = M
M = D

@SP
M = M+1 
@SP
A = M-1
M = -M

//**push constant**
@1
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

//**push constant**
@32767
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
A = M-1
M = -M

//**push constant**
@1
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
AM = M-1
D = M
@Yltz.2
D;JLT            
@SP       
A = M-1
D = M
@false.2 
D;JLT          
(sub.2)  
@SP
A = M
D = D-M
@true.2
D;JGT
@false.2
0;JMP
(Yltz.2)
@SP
A = M-1
D = M
@true.2
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
@20000
D = A

@SP
A = M
M = D

@SP
M = M+1 
@SP
A = M-1
M = -M

//**push constant**
@1
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
//**push constant**
@30000
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
@20000
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@30000
D = A

@SP
A = M
M = D

@SP
M = M+1 
@SP
A = M-1
M = -M

//**push constant**
@1
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
AM = M-1
D = M
@Yltz.4
D;JLT            
@SP       
A = M-1
D = M
@false.4 
D;JLT          
(sub.4)  
@SP
A = M
D = D-M
@true.4
D;JGT
@false.4
0;JMP
(Yltz.4)
@SP
A = M-1
D = M
@true.4
D;JGE
@sub.4
0;JMP

(true.4)
@SP
A = M-1
M = -1
@end.4
0;JMP

(false.4)
@SP
A = M-1
M = 0

(end.4) 
