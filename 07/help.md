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