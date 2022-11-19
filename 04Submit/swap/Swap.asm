// This file is part of nand2tetris, as taught in The Hebrew University, and
// was written by Aviv Yaish. It is an extension to the specifications given
// [here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
// as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
// Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

// The program should swap between the max. and min. elements of an array.
// Assumptions:
// - The array's start address is stored in R14, and R15 contains its length
// - Each array value x is between -16384 < x < 16384
// - The address in R14 is at least >= 2048
// - R14 + R15 <= 16383
//
// Requirements:
// - Changing R14, R15 is not allowed.

// Put your code here.

//init


//init temp min
//init temp min address
@R14
D = M

@minA
M = D
@maxA
M = D
@currA
M = D

@minA
A = M   
D = M

@minV
M = D
@maxV
M = D
@currV //init curr address in array
M = D

//init lastAdres = R14 + arrLenght
@R15
D = M
@R14
D = D + M

@lstA
M = D-1 //last add still legal

//main loop runs on array
(LOOP)

    //if curr < min or curr > max
    //change min / max and adress accordingly
    @currV
    D = M
    @minV
    D = D - M

    @UPDATE_MIN
    D;JLT


    @currV
    D = M
    @maxV
    D = D - M

    @UPDATE_MAX
    D;JGT


    @INCREASE
    0;JMP


(UPDATE_MIN)
    @currV
    D = M
    @minV
    M = D

    @currA
    D = M
    @minA
    M = D
    
    @INCREASE
    0;JMP



(UPDATE_MAX)
    @currV
    D = M
    @maxV
    M = D

    @currA
    D = M
    @maxA
    M = D

    @INCREASE
    0;JMP

(INCREASE)
    //check if curr adres > last address:
    //if yes, go to swap
    @currA
    D = M
    @lstA
    D = D - M

    @SWAP
    D;JGE

    //curr address ++
    @currA
    M = M+1

    @currA
    A = M
    D = M

    @currV
    M = D

    @LOOP
    0;JMP


(SWAP)
    @minV
    D = M

    @maxA
    A = M
    M = D

    @maxV
    D = M

    @minA
    A = M
    M = D


(END)
    @END
    0;JMP
//swap
//init buffer = temp min
//temp min = temp max
//temp max = temp min