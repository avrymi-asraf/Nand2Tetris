//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1//**eq**
@SP
AM = M-1
D = M   //old value
A = A-1
D = D-M //the difference 
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
@17
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@16
D = A

@SP
A = M
M = D

@SP
M = M+1//**eq**
@SP
AM = M-1
D = M   //old value
A = A-1
D = D-M //the difference 
@eq.2
D;JEQ       //if is not equal         
@SP          //else
A = M-1
M = 0
@end.2
0;JMP
(eq.2) //set to true  
    @SP
    A = M-1
    M = -1
(end.2)
//**push constant**
@16
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@17
D = A

@SP
A = M
M = D

@SP
M = M+1//**eq**
@SP
AM = M-1
D = M   //old value
A = A-1
D = D-M //the difference 
@eq.3
D;JEQ       //if is not equal         
@SP          //else
A = M-1
M = 0
@end.3
0;JMP
(eq.3) //set to true  
    @SP
    A = M-1
    M = -1
(end.3)
//**push constant**
@892
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1//**lt**
@SP
AM = M-1
D = M
@Yltz.4
D;JLT            
@SP       
A = M-1
D = M
@true.4 
D;JLT          
(sub.4)  
@SP
A = M
D = D-M
@false.4
D;JGE
@true.4
0;JMP
(Yltz.4)
@SP
A = M-1
D = M
@false.4
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
//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@892
D = A

@SP
A = M
M = D

@SP
M = M+1//**lt**
@SP
AM = M-1
D = M
@Yltz.5
D;JLT            
@SP       
A = M-1
D = M
@true.5 
D;JLT          
(sub.5)  
@SP
A = M
D = D-M
@false.5
D;JGE
@true.5
0;JMP
(Yltz.5)
@SP
A = M-1
D = M
@false.5
D;JGE
@sub.5
0;JMP

(true.5)
@SP
A = M-1
M = -1
@end.5
0;JMP

(false.5)
@SP
A = M-1
M = 0

(end.5) 
//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@891
D = A

@SP
A = M
M = D

@SP
M = M+1//**lt**
@SP
AM = M-1
D = M
@Yltz.6
D;JLT            
@SP       
A = M-1
D = M
@true.6 
D;JLT          
(sub.6)  
@SP
A = M
D = D-M
@false.6
D;JGE
@true.6
0;JMP
(Yltz.6)
@SP
A = M-1
D = M
@false.6
D;JGE
@sub.6
0;JMP

(true.6)
@SP
A = M-1
M = -1
@end.6
0;JMP

(false.6)
@SP
A = M-1
M = 0

(end.6) 
//**push constant**
@32767
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1//**gt**
//**C_gt**
@SP
AM = M-1
D = M
@Yltz.7
D;JLT            
@SP       
A = M-1
D = M
@false.7 
D;JLT          
(sub.7)  
@SP
A = M
D = D-M
@true.7
D;JGT
@false.7
0;JMP
(Yltz.7)
@SP
A = M-1
D = M
@true.7
D;JGE
@sub.7
0;JMP

(true.7)
@SP
A = M-1
M = -1
@end.7
0;JMP

(false.7)
@SP
A = M-1
M = 0

(end.7) 
//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@32767
D = A

@SP
A = M
M = D

@SP
M = M+1//**gt**
//**C_gt**
@SP
AM = M-1
D = M
@Yltz.8
D;JLT            
@SP       
A = M-1
D = M
@false.8 
D;JLT          
(sub.8)  
@SP
A = M
D = D-M
@true.8
D;JGT
@false.8
0;JMP
(Yltz.8)
@SP
A = M-1
D = M
@true.8
D;JGE
@sub.8
0;JMP

(true.8)
@SP
A = M-1
M = -1
@end.8
0;JMP

(false.8)
@SP
A = M-1
M = 0

(end.8) 
//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@32766
D = A

@SP
A = M
M = D

@SP
M = M+1//**gt**
//**C_gt**
@SP
AM = M-1
D = M
@Yltz.9
D;JLT            
@SP       
A = M-1
D = M
@false.9 
D;JLT          
(sub.9)  
@SP
A = M
D = D-M
@true.9
D;JGT
@false.9
0;JMP
(Yltz.9)
@SP
A = M-1
D = M
@true.9
D;JGE
@sub.9
0;JMP

(true.9)
@SP
A = M-1
M = -1
@end.9
0;JMP

(false.9)
@SP
A = M-1
M = 0

(end.9) 
//**push constant**
@57
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@31
D = A

@SP
A = M
M = D

@SP
M = M+1//**push constant**
@53
D = A

@SP
A = M
M = D

@SP
M = M+1//**add**
@SP
AM = M-1
D = M
A = A-1
M = M + D
//**push constant**
@112
D = A

@SP
A = M
M = D

@SP
M = M+1//**sub**
@SP
AM=M-1
D=M
A = A-1
M = M-D
//**neg**
@SP
A = M-1
M = -M
//**and**
@SP
AM = M-1
D = M
A = A-1
M = D&M
//**push constant**
@82
D = A

@SP
A = M
M = D

@SP
M = M+1//**or**  
@SP
AM = M-1
D = M
A = A-1
M = D|M
    //**not**
@SP
A = M-1
M = !M
    