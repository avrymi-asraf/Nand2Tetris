"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
from typing import Optional
import cons

TYPEIND = 0
KINDIND = 1
INDEXIND = 2


class SymbolTable:
    """A symbol table that associates names with information ne eded for Jack
    compilation: type, kind and running index. The symbol table has two nested
    scopes (class/subroutine).
    """

    def __init__(self) -> None:
        """Creates a new empty symbol table."""

        # name, type, kind, ind
        self.subroutineStable: cons.SymbolTableType = {}
        self.classStable: cons.SymbolTableType = {}

    def start_subroutine(self) -> None:
        """Starts a new subroutine scope (i.e., resets the subroutine's
        symbol table).
        """
        self.subroutineStable.clear()

    def define(
        self, name: str, var_type: str, kind: cons.VarKindType
    ) -> None:
        """Defines a new identifier of a given name, type and kind and assigns
        it a running index. "STATIC" and "FIELD" identifiers have a class scope,
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """
        if kind in {cons.STATIC, cons.FIELD}:
            # class scope
            self.classStable[name] = (
                var_type,
                kind,
                self.var_count(kind),
            )

            # type: ignore
        elif kind in {cons.ARG, cons.VAR}:
            # subroutine scope
            self.subroutineStable[name] = (
                var_type,
                kind,
                self.var_count(kind),
            )
        else:
            raise ValueError("unknown variable {}".format(name))

    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in
            the current scope.
        """
        counter = 0

        if kind in {cons.STATIC, cons.FIELD}:
            # class scope
            for val in self.classStable.values():
                if val[KINDIND] == kind:
                    counter += 1

        elif kind in {cons.ARG, cons.VAR}:
            # subroutine scope
            for val in self.subroutineStable.values():
                if val[KINDIND] == kind:
                    counter += 1
        else:
            raise ValueError("unknown kind {}".format(kind))

        return counter

    def kind_of(self, name: str) -> Optional[cons.VarKindType]:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        if name in self.subroutineStable:
            return self.subroutineStable[name][KINDIND]

        elif name in self.classStable:
            return self.classStable[name][KINDIND]

        else:
            return None

    def type_of(self, name: str) -> str:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        if name in self.subroutineStable:
            return self.subroutineStable[name][TYPEIND]
        elif name in self.classStable:
            return self.classStable[name][TYPEIND]
        else:
            raise ValueError("unknown variable {}".format(name))

    def index_of(self, name: str) -> int:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        if name in self.subroutineStable:
            return self.subroutineStable[name][INDEXIND]

        if name in self.classStable:
            return self.classStable[name][INDEXIND]

        raise ValueError("unknown variable {}".format(name))

    def kind_of_as_segment(self, name: str) -> cons.SegmentType:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        if name in self.subroutineStable:
            return cons.kind_to_segment[
                self.subroutineStable[name][KINDIND]
            ]

        if name in self.classStable:
            return cons.kind_to_segment[
                self.classStable[name][KINDIND]
            ]
        raise ValueError("unknown variable {}".format(name))

    def num_of_kind(self, kind: cons.VarKindType) -> int:
        '''
        return the number of variables in the given kind

        Args:
            kind (cons.VarKindType): kind of the variable

        Raises:
            ValueError: if the kind is not known

        Returns:
            int: number of variables in the given kind
        '''
        #TODO: what if symbol table is empty?
        if kind in {cons.STATIC, cons.FIELD}:
            # class scope
            return len(
                list(
                    filter(
                        lambda i: i[KINDIND] == kind,
                        self.classStable.items(),
                    )
                )
            )
        elif kind in {cons.ARG, cons.VAR}:
            # subroutine scope
            return len(
                list(
                    filter(
                        lambda i: i[KINDIND] == kind,
                        self.subroutineStable.items(),
                    )
                )
            )
        raise ValueError("{} this is not a kind".format(kind))
