
//**push constant**
@0
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
@2
D = A

@SP
A = M
M = D

@SP
M = M+1