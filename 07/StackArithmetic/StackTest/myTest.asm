
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
@tltz.1   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@false.1      // if second argument < 0  
D;JLT 
@sub.1   //else sub them
0;JMP
(tltz.1)
    @SP
    A = M -1
    D = M
    @true.1 // if second argument >0
    D;JGT      
    @sub.1    //else sub them 
    0;JMP
(sub.1)
    @SP
    A = M 
    D = D-M //D second argument, M first argument
    @true.1
    D;JGT 
    @false.1 //else true
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
