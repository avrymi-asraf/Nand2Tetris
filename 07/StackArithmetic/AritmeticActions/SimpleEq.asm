
//push
@8
D = A
@SP
A = M
M = D

@SP
M =M+1
//push
@8
D = A
@SP
A = M
M = D

@SP
M =M+1
@SP
AM = M-1
D = M

A = A-1
D = D-M

@EQ
D;JEQ
//if is not equal 
@0
D = A
@SP
A = M-1
M = D

@END
0;JMP

(EQ)
    @1
    D = -A
    @SP
    A = M-1
    M = D
(END)
@1
