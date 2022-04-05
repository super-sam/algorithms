import stack
from typing import Any

class StackMax(stack.Stack):
    __stack_max: stack.Stack = stack.Stack()

    def push(self, item: Any) -> None:
        if not self.is_empty() and self.peek() > item:
            self.__stack_max.push(self.peek())
        else:
            self.__stack_max.push(item)
        return super().push(item)
    
    def pop(self) -> Any:
        self.__stack_max.pop()
        return super().pop()
    
    def max(self) -> Any:
        return self.__stack_max.peek()
    
    def items(self):
        return self.__stack_max

if __name__ == '__main__':
    s = StackMax()
    s.push(1)
    s.push(2)
    s.push(20)
    s.push(10)


    
    