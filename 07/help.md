The compiler uses a 2-place memory segment called pointer
for storing the current base addresses of this and that
Implementation \
• To push/pop pointer 0, generate assembly code that executes push/pop THIS \
• To push/pop pointer 1, generate assembly code that executes push/pop THAT 


LCL, ARG, THIS, THAT
The temp segment is stored in a fixed RAM block, from address 5 to 12



```
if segment == "temp":
    index += 5
    address = "R5"
    self.__file.write(
        "@" + address + "\nD=M\n@" + str(index) + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
elif segment == "pointer":
    if index == 0:
        address = "THIS"
        self.__file.write(
            "@" + address + "\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
    if index == 1:
        address = "THAT"
        self.__file.write(
            "@" + address + "\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n")
            ```


```
    "SCREEN":"16384",
    "KBD":"24576",
    "SP":"0",
    "LCL":"1",
    "ARG":"2",
    "THIS":"3",
    "THAT":"4"
```



```
@SP
AM = M-1
D = M
@Yltz._counter
D;JLT            
@SP       
A = M-1
D = M
@false._counter 
D;JLT          
(sub._counter)  
@SP
A = M
D = D-M
@true._counter
D;JGT
@false._counter
0;JMP
(Yltz._counter)
@SP
A = M-1
D = M
@true._counter
D;JGE
@sub._counter
0;JMP

(true._counter)
@SP
A = M-1
M = -1
@end._counter
0;JMP

(false._counter)
@SP
A = M-1
M = -1

(end._counter) 
```



```
@SP
AM = M-1
D = M
@Yltz._counter
D;JLT            
@SP       
A = M-1
D = M
@true._counter 
D;JGT          
(sub._counter)  
@SP
A = M
D = D-M
@false._counter
D;JGE
@true._counter
0;JMP
(Yltz._counter)
@SP
A = M-1
D = M
@false._counter
D;JGE
@sub._counter
0;JMP

(true._counter)
@SP
A = M-1
M = -1
@end._counter
0;JMP

(false._counter)
@SP
A = M-1
M = 0

(end._counter) 
```