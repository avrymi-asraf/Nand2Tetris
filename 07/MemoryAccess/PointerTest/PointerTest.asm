
//**push constant**
@3030
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside pointer at the given 0
@0
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@3040
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside pointer at the given 1
@1
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@32
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside this at the given 2
@2
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@46
D = A

@SP
A = M
A = A-1 //added now
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M
A = A-1 //added now
D = M

//write data inside that at the given 6
@6
M = D

//decrement SP
@SP
M = M-1


//**push argument**
//go to pointer at 0

@pointer
D = M

@0
D = D+A

A = D
D = M

// write in SP
@SP
A = M
A = A-1 //added now
M = D

// inc SP
@SP
M = M+1
//**push argument**
//go to pointer at 1

@pointer
D = M

@1
D = D+A

A = D
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
//**push argument**
//go to this at 2

@this
D = M

@2
D = D+A

A = D
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
//**push argument**
//go to that at 6

@that
D = M

@6
D = D+A

A = D
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