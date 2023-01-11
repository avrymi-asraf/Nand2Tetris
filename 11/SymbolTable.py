"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import Constants
from typing import Dict, Optional,Tuple

TYPEIND = 0
KINDIND = 1
INDEXIND = 2


class SymbolTable:
    """A symbol table that associates names with information needed for Jack
    compilation: type, kind and running index. The symbol table has two nested
    scopes (class/subroutine).
    """
    
    subroutineStable:Constants.SymbolTableType = {}
    classStable:Constants.SymbolTableType = {}

    def __init__(self) -> None:
        """Creates a new empty symbol table."""

        #name, type, kind, ind
        self.subroutineStable = {}
        self.classStable = {}

    def start_subroutine(self) -> None:
        """Starts a new subroutine scope (i.e., resets the subroutine's 
        symbol table).
        """
        self.subroutineStable.clear()

    def define(self, name: str, type: str, kind: str) -> None:
        """Defines a new identifier of a given name, type and kind and assigns 
        it a running index. "STATIC" and "FIELD" identifiers have a class scope, 
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """
        if (kind in {"STATIC", "FIELD"}):
            #class scope
            self.classStable[name] = tuple(type, kind, self.var_count(kind) +1 ) 

            # type: ignore
        elif (kind in {"ARG", "VAR"}):
            #subroutine scope
            self.subroutineStable[name] = tuple(type, kind, self.var_count(kind) +1 ) 
    
    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in 
            the current scope.
        """
        counter = 0

        if (kind in {"STATIC", "FIELD"}):
            #class scope
            for val in self.classStable.values():
                if (val[KINDIND] == kind):
                    counter+=1

        elif (kind in {"ARG", "VAR"}):
            #subroutine scope
            for val in self.subroutineStable.values():
                if (val[KINDIND] == kind):
                    counter+=1
        
        return counter

    def kind_of(self, name: str) -> Optional[str]:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        if (name in self.subroutineStable):
            return self.subroutineStable[name][KINDIND]
        
        if (name in self.classStable):
            return self.classStable[name][KINDIND]

        return None

    def type_of(self, name: str) ->  Optional[str]:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        if (name in self.subroutineStable):
            return self.subroutineStable[name][TYPEIND]
        
        if (name in self.classStable):
            return self.classStable[name][TYPEIND]
            
        return None


    def index_of(self, name: str) ->  Optional[int]:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        if (name in self.subroutineStable):
            return self.subroutineStable[name][INDEXIND]
        
        if (name in self.classStable):
            return self.classStable[name][INDEXIND]
            
        return None



