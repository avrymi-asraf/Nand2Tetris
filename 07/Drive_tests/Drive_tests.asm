
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
@tltz.2  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.2   // if second argument < 0  
D;JLT 
@subthem.2 //else sub them
0;JMP
(tltz.2)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.2  // if second argument >= 0
    D;JGE     
    @subthem.2  //else sub them  
    0;JMP
(subthem.2)
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
@tltz.3   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.3      // if second argument < 0  
D;JLT 
@subthem.3   //else sub them
0;JMP
(tltz.3)
    @SP
    A = M -1
    D = M
    @false.3 // if second argument >0
    D;JGT      
    @subthem.3    //else sub them 
    0;JMP
(subthem.3)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.3
    D;JGE 
    @true.3 //else true
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
@tltz.2  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.2   // if second argument < 0  
D;JLT 
@subthem.2 //else sub them
0;JMP
(tltz.2)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.2  // if second argument >= 0
    D;JGE     
    @subthem.2  //else sub them  
    0;JMP
(subthem.2)
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
@tltz.3   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.3      // if second argument < 0  
D;JLT 
@subthem.3   //else sub them
0;JMP
(tltz.3)
    @SP
    A = M -1
    D = M
    @false.3 // if second argument >0
    D;JGT      
    @subthem.3    //else sub them 
    0;JMP
(subthem.3)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.3
    D;JGE 
    @true.3 //else true
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
    
//**push constant**
@100
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop static**

//take data from top of stack
@SP
A = M 

A = A-1
D = M

//write data inside segment at the given T2.8
@T2.8
M = D

//decrement SP
@SP
M = M-1


//**push static**
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@T2.8
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1
//**push constant**
@3030
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@3
D = M

@0
D = D + A

@_temp_0
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_0
A = M
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@3040
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@3
D = M

@1
D = D + A

@_temp_1
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_1
A = M
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@32
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@THIS
D = M

@2
D = D + A

@_temp_2
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_2
A = M
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@46
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@THAT
D = M

@6
D = D + A

@_temp_6
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_6
A = M
M = D

//decrement SP
@SP
M = M-1


//**push argument**
//go to 3 at 0

@3
D = M

@0
D = D+A

A = D
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1
//**push argument**
//go to 3 at 1

@3
D = M

@1
D = D+A

A = D
D = M

// write in SP
@SP
A = M
M = D

// inc SP
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
//**push argument**
//go to THIS at 2

@THIS
D = M

@2
D = D+A

A = D
D = M

// write in SP
@SP
A = M
M = D

// inc SP
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
//**push argument**
//go to THAT at 6

@THAT
D = M

@6
D = D+A

A = D
D = M

// write in SP
@SP
A = M
M = D

// inc SP
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
@3038
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@3
D = M

@0
D = D + A

@_temp_0
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_0
A = M
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@15
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@THIS
D = M

@2
D = D + A

@_temp_2
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_2
A = M
M = D

//decrement SP
@SP
M = M-1


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
@tltz.1  // if first argument < 0    
D;JLT
@SP             //else first > 0  
A = M-1
D = M
@false.1   // if second argument < 0  
D;JLT 
@subthem.1 //else sub them
0;JMP
(tltz.1)    // first argument < 0
    @SP
    A = M-1         
    D = M           //D hold the second argument
    @true.1  // if second argument >= 0
    D;JGE     
    @subthem.1  //else sub them  
    0;JMP
(subthem.1)
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
@tltz.2   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.2      // if second argument < 0  
D;JLT 
@subthem.2   //else sub them
0;JMP
(tltz.2)
    @SP
    A = M -1
    D = M
    @false.2 // if second argument >0
    D;JGT      
    @subthem.2    //else sub them 
    0;JMP
(subthem.2)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.2
    D;JGE 
    @true.2 //else true
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
@tltz.3   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.3      // if second argument < 0  
D;JLT 
@subthem.3   //else sub them
0;JMP
(tltz.3)
    @SP
    A = M -1
    D = M
    @false.3 // if second argument >0
    D;JGT      
    @subthem.3    //else sub them 
    0;JMP
(subthem.3)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.3
    D;JGE 
    @true.3 //else true
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
@tltz.4   // if first argument < 0    
D;JLT
@SP     //else first argument > 0  
A = M-1
D = M
@true.4      // if second argument < 0  
D;JLT 
@subthem.4   //else sub them
0;JMP
(tltz.4)
    @SP
    A = M -1
    D = M
    @false.4 // if second argument >0
    D;JGT      
    @subthem.4    //else sub them 
    0;JMP
(subthem.4)
    @SP
    A = M -1
    D = M-D //D second argument, M first argument
    @false.4
    D;JGE 
    @true.4 //else true
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
