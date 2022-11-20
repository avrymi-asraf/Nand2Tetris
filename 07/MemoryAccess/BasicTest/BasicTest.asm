
//**push constant**
@10
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@local
D = M

@0
D = D+A

@_temp_0
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_0
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

//find address
@argument
D = M

@2
D = D+A

@_temp_2
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_2
M = D

//decrement SP
@SP
M = M-1

 
//**pop argument**

//find address
@argument
D = M

@1
D = D+A

@_temp_1
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_1
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

//find address
@this
D = M

@6
D = D+A

@_temp_6
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_6
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

//find address
@that
D = M

@5
D = D+A

@_temp_5
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_5
M = D

//decrement SP
@SP
M = M-1

 
//**pop argument**

//find address
@that
D = M

@2
D = D+A

@_temp_2
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_2
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

//find address
@temp
D = M

@6
D = D+A

@_temp_6
M = D

//take data from top of stack
@SP
A = M - 1 
D = M

@_temp_6
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