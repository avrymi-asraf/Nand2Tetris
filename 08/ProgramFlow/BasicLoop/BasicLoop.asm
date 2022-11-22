
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

