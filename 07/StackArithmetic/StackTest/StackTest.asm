
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
D = M   //old value
A = A-1
D = D-M // the difference
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
@tltz.4  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.4   // if second argument < 0  
D;JLT 
@subthem.4 //else sub them
0;JMP
(tltz.4)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.4  // if second argument >= 0
    D;JGE     
    @subthem.4  //else sub them  
    0;JMP
(subthem.4)
    @SP
    A = M 
    D = M-D     //second argument - first argument
    @true.4  
    D;JGT
    @false.4 //else false
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
@tltz.5  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.5   // if second argument < 0  
D;JLT 
@subthem.5 //else sub them
0;JMP
(tltz.5)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.5  // if second argument >= 0
    D;JGE     
    @subthem.5  //else sub them  
    0;JMP
(subthem.5)
    @SP
    A = M 
    D = M-D     //second argument - first argument
    @true.5  
    D;JGT
    @false.5 //else false
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
@tltz.6  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.6   // if second argument < 0  
D;JLT 
@subthem.6 //else sub them
0;JMP
(tltz.6)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.6  // if second argument >= 0
    D;JGE     
    @subthem.6  //else sub them  
    0;JMP
(subthem.6)
    @SP
    A = M 
    D = M-D     //second argument - first argument
    @true.6  
    D;JGT
    @false.6 //else false
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
@tltz.7   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.7      // if second argument < 0  
D;JLT 
@subthem.7   //else sub them
0;JMP
(tltz.7)
    @SP
    A = M -1
    D = M
    @false.7 // if second argument >0
    D;JGT      
    @subthem.7    //else sub them 
    0;JMP
(subthem.7)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.7
    D;JGE 
    @true.7 //else true
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
@tltz.8   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.8      // if second argument < 0  
D;JLT 
@subthem.8   //else sub them
0;JMP
(tltz.8)
    @SP
    A = M -1
    D = M
    @false.8 // if second argument >0
    D;JGT      
    @subthem.8    //else sub them 
    0;JMP
(subthem.8)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.8
    D;JGE 
    @true.8 //else true
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
@tltz.9   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.9      // if second argument < 0  
D;JLT 
@subthem.9   //else sub them
0;JMP
(tltz.9)
    @SP
    A = M -1
    D = M
    @false.9 // if second argument >0
    D;JGT      
    @subthem.9    //else sub them 
    0;JMP
(subthem.9)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.9
    D;JGE 
    @true.9 //else true
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
    
@SP
A = M-1
M = !M
    