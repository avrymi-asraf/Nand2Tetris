from typing import Tuple
import random

LOC_SCREEN = 16384  

def loc_in_ram(row:int,col:int)->Tuple[int,int]:
    """
    return tuple containing word and bit in word
    """
    return 32*row+col//16, col%16






