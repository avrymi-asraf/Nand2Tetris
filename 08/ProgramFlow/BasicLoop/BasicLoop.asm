
//**push constant**
@0
D = A

@SP
A = M
M = D

@SP
M = M+1 
//**pop argument**

//find address
@LCL
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

(main$LOOP_START)
//**push argument**
//go to ARG at 0

@ARG
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
//go to LCL at 0

@LCL
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
//**add**
@SP
AM=M-1
D=M

@SP 
AM = M-1
M = D+M

@SP
M =M+1 
//**pop argument**

//find address
@LCL
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


//**push argument**
//go to ARG at 0

@ARG
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
//**pop argument**

//find address
@ARG
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


//**push argument**
//go to ARG at 0

@ARG
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
M = M+1"
@SP
A = M-1
D = M

@main$LOOP_START
D;JLT
D;JGT

//**push argument**
//go to LCL at 0

@LCL
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