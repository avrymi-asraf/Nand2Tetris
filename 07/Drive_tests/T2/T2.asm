
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
A = M -1
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
    //**pop this that**
@SP
A = M-1      
D = M

@THIS
M = D

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
    //**pop this that**
@SP
A = M-1      
D = M

@THAT
M = D

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


     //**push this that**
@THIS
D = M

@SP         
A=M
M = D

@SP
M=M+1
    
     //**push this that**
@THAT
D = M

@SP         
A=M
M = D

@SP
M=M+1
    
//**add**
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
@3038
D = A

@SP
A = M
M = D

@SP
M = M+1
    //**pop this that**
@SP
A = M-1      
D = M

@THIS
M = D

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

