
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

@eq
D;JEQ
 
@0
D = A
@SP
A = M-1
M = D

@end
0;JMP

(eq)
@-1
D = A
@SP
A = M-1
M = D


(end)
