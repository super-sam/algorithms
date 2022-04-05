from typing import Any
import stack_abstract

class ArrayStack(stack_abstract.StackAbstract):
    __stack: Any
    __index: int = 0

    def __init__(self, capacity: int) -> None:
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
        return item
    
    def push(self, item: Any) -> None:
        if self.is_full():
            raise IndexError("Stack is full")

        self.__stack[self.__index] = item
        self.__index += 1

if __name__ == "__main__":
    array_list: ArrayStack = ArrayStack(5)
    array_list.push("1")
    array_list.push("2")
    array_list.push("3")
    array_list.push("4")
    
    print(array_list.is_empty())
    print(array_list.pop())
    print(array_list.pop())
    print(array_list.pop())
    print(array_list.is_empty())

    array_listInt: ArrayStack = ArrayStack(5)
    array_listInt.push(1)
    array_listInt.push(2)
    array_listInt.push(3)
    print(array_listInt.is_empty())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.pop())
    print(array_listInt.is_empty())
    print(array_listInt.pop())

