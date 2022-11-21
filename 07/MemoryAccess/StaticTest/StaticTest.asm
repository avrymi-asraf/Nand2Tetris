
//**push constant**
@111
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@333
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@888
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

//write data inside segment at the given StaticTest.8
@StaticTest.8
M = D

//decrement SP
@SP
M = M-1

 
//**pop static**

//take data from top of stack
@SP
A = M -1
D = M

//write data inside segment at the given StaticTest.3
@StaticTest.3
M = D

//decrement SP
@SP
M = M-1

 
//**pop static**

//take data from top of stack
@SP
A = M -1
D = M

//write data inside segment at the given StaticTest.1
@StaticTest.1
M = D

//decrement SP
@SP
M = M-1


//**push static**
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@StaticTest.3
D = M

// write in SP
@SP
A = M
M = D

// inc SP
@SP
M = M+1
//**push static**
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@StaticTest.1
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
//**push static**
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@StaticTest.8
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