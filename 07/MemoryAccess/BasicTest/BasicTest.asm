
//**push constant**
@10
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside local at the given 0
@0
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@21
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@22
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside argument at the given 2
@2
M = D

//decrement SP
@SP
M = M-1

 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside argument at the given 1
@1
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@36
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside this at the given 6
@6
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@42
D = A

@SP
A = M
M = D

@SP
M = M+1
//**push constant**
@45
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside that at the given 5
@5
M = D

//decrement SP
@SP
M = M-1

 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside that at the given 2
@2
M = D

//decrement SP
@SP
M = M-1


//**push constant**
@510
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//take data from top of stack
@SP
A = M - 1 
D = M

//write data inside temp at the given 6
@6
M = D

//decrement SP
@SP
M = M-1


//**push argument**
//go to local at 0

@local
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
//go to that at 5

@that
D = M

@5
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
//go to argument at 1

@argument
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
M = M-D

@SP
M =M+1
//**push argument**
//go to this at 6

@this
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
//**push argument**
//go to this at 6

@this
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
//go to temp at 6

@temp
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