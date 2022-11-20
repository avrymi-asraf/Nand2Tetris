
//**push constant**
@111
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1
//**push constant**
@333
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1
//**push constant**
@888
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1 
//**pop static**

//find address :  segment at StaticTest.8
@segment
D = M

@StaticTest.8
D=D+A

@_temp_StaticTest.8
M = D

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside segment at the given StaticTest.8
@_temp_StaticTest.8
M = D

//decrement SP
@SP
M =M-1

 
//**pop static**

//find address :  segment at StaticTest.3
@segment
D = M

@StaticTest.3
D=D+A

@_temp_StaticTest.3
M = D

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside segment at the given StaticTest.3
@_temp_StaticTest.3
M = D

//decrement SP
@SP
M =M-1

 
//**pop static**

//find address :  segment at StaticTest.1
@segment
D = M

@StaticTest.1
D=D+A

@_temp_StaticTest.1
M = D

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside segment at the given StaticTest.1
@_temp_StaticTest.1
M = D

//decrement SP
@SP
M =M-1


//**push static**
//go to static at the symbol "Xxx.i". write it in the top of the stack 

@StaticTest.3
D = M

// write in SP
@SP
A = M
A = A-1 //added now
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
A = A-1 //added now
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
A = A-1 //added now
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