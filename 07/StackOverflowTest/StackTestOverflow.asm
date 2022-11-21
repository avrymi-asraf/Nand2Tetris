
//**push constant**
@0
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
@2
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
@tltz.1  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.1   // if second argument < 0  
D;JLT 
@sub.1 //else sub them
0;JMP
(tltz.1)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.1  // if second argument >= 0
    D;JGE     
    @sub.1  //else sub them  
    0;JMP
(sub.1)
    @SP
    A = M 
    D = M-D     //second argument - first argument
    @true.1  
    D;JGT
    @false.1 //else false
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
@2
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@0
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
@tltz.2  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.2   // if second argument < 0  
D;JLT 
@sub.2 //else sub them
0;JMP
(tltz.2)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.2  // if second argument >= 0
    D;JGE     
    @sub.2  //else sub them  
    0;JMP
(sub.2)
    @SP
    A = M 
    D = M-D     //second argument - first argument
    @true.2  
    D;JGT
    @false.2 //else false
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
@0
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
@2
D = A

@SP
A = M
M = D

@SP
M = M+1
@SP 
AM = M-1
D = M
@tltz.3   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@false.3      // if second argument < 0  
D;JLT 
@sub.3   //else sub them
0;JMP
(tltz.3)
    @SP
    A = M 
    D = M
    @true.3 // if second argument >0
    D;JGT      
    @sub.3    //else sub them 
    0;JMP
(sub.3)
    @SP
    A = M 
    D = D-M //D second argument, M first argument
    @true.3
    D;JGT 
    @false.3 //else true
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
@2
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@0
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
@tltz.4   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@false.4      // if second argument < 0  
D;JLT 
@sub.4   //else sub them
0;JMP
(tltz.4)
    @SP
    A = M 
    D = M
    @true.4 // if second argument >0
    D;JGT      
    @sub.4    //else sub them 
    0;JMP
(sub.4)
    @SP
    A = M 
    D = D-M //D second argument, M first argument
    @true.4
    D;JGT 
    @false.4 //else true
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
