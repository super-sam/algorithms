from typing import Any
import stack_abstract


class ArrayStack(stack_abstract.StackAbstract):
    __stack: Any
    __index: int = 0

    @property
    def length(self) -> int:
        return self.__index

    def __init__(self, capacity=1) -> None:
        self.__stack = [None] * capacity

    def is_empty(self) -> bool:
        return self.__index == 0
    
    def is_full(self) -> bool:
        return self.__index == len(self.__stack)
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is Empty")
        
        return self.__stack[self.__index - 1]
    
    def pop(self) -> Any:
        item: Any = self.peek()
        self.__stack[self.__index - 1] = None
        self.__index -= 1
        if self.__index <= len(self.__stack) // 4:
            del self.__stack[len(self.__stack) // 2 : ]
        return item
    
    def push(self, item: Any) -> None:
        if self.is_full():
            self.__stack.extend([None] * len(self.__stack))

        self.__stack[self.__index] = item
        self.__index += 1
    
    def __str__(self) -> str:
        return f'[{", ".join(map(str, self.__stack))}]'

if __name__ == "__main__":
    array_listInt: ArrayStack = ArrayStack()
    array_listInt.push(1)
    array_listInt.push(2)
    array_listInt.push(3)
    array_listInt.push(4)
    array_listInt.push(5)
    array_listInt.push(6)
    array_listInt.push(7)
    array_listInt.push(8)
    print(array_listInt.is_empty())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.is_empty())
    print(array_listInt.pop())

