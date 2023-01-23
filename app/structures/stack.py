from __future__ import annotations
from typing import Generic, Iterable, Optional, Union
from app.structures.data_common import Datas, T
from app.structures.exceptions import PopException


class Stack(Generic[T]):

    def __init__(self, initial_stack: Union[T, Iterable[T]] = None) -> None:
        self._length: int = 0
        self.head: Optional[Datas] = None

        if initial_stack:
            if isinstance(initial_stack, (list, tuple)):
                for value in initial_stack:
                    self.push(value)
            else:
                self.push(initial_stack)

    def push(self, data: Union[T, Iterable[T]]) -> None:
        """
        Pushes a generic data into the stack.

        :param data:
        :return: None
        """

        aux: Optional[Datas] = self.head
        self.head = Datas()
        self.head.item = data
        self.head.next = aux
        self._length += 1

    def pop(self) -> Optional[T]:
        """
        Pops a generic data out of the stack.

        :return: Optional[T]
        """
        if self.is_empty():
            raise PopException()

        data: Optional[T] = None

        if self.head:
            data = self.head.item
            self.head = self.head.next
            self._length -= 1

        return data

    def pop_all(self) -> None:
        """
        remove all items from the stack.

        :return: None
        """
        while True:
            try:
                self.pop()
            except PopException:
                break

    def is_empty(self) -> bool:
        """
        Indicates if the stack is empty.

        :return: bool
        """
        return self.head is None

    @staticmethod
    def print(stack: Stack) -> str:
        """
        String representation of the stack.

        :param stack:
        :return: str
        """
        current: Optional[Datas] = stack.head
        as_string: str = ''

        while current:
            as_string += f'{str(current.item)} -> '
            current = current.next

        return as_string[:-4]

    def __len__(self) -> int:
        """
        Returns the stack's length.

        :return: int
        """
        return self._length

    def __repr__(self) -> str:
        """
        Stack representation is a string.

        :return: str
        """
        return Stack.print(self)

    def __str__(self) -> str:
        """
        Stack representation is a string.

        :return: str
        """
        return Stack.print(self)
