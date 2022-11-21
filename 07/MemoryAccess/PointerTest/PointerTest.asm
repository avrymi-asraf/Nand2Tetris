
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
"@THIS
D = M

@SP         
A=M
M = D

@SP
M=M+1
    
     //**push this that**
"@THAT
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