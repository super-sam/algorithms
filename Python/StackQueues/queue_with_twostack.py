from typing import Any
import stack

class QueueWithStacks:
    __stack_in: stack.Stack= stack.Stack()
    __stack_out: stack.Stack= stack.Stack()

    def is_empty(self) -> bool:
        return self.__stack_in.is_empty() and self.__stack_out.is_empty()
    
    def peek(self) -> Any:
        """Returns the first inserted item
        Raises:
            IndexError: When queue is empty
        Returns:
            The first inserted item
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        if self.__stack_out.is_empty():
            while not self.__stack_in.is_empty():
                self.__stack_out.push(self.__stack_in.pop())
        
        return self.__stack_out.peek()
    
    def enque(self, item: Any) -> None:
        self.__stack_in.push(item)
    
    def deque(self) -> Any:
        """Deletes the first inserted item and returns it
        Raises:
            IndexError: When queue is empty
        Returns:
            The first inserted item
        """
        item = self.peek()
        self.__stack_out.pop()
        return item

if __name__ == '__main__':
    q = QueueWithStacks()
    q.enque(1)
    q.enque(2)
    print(q.peek())
    q.enque(3)
    q.enque(4)
    q.enque(5)
    print(q.deque(), q._QueueWithStacks__stack_in, q._QueueWithStacks__stack_out)
    print(q.deque(), q._QueueWithStacks__stack_in, q._QueueWithStacks__stack_out)
    print(q.deque(), q._QueueWithStacks__stack_in, q._QueueWithStacks__stack_out)
    print(q.deque(), q._QueueWithStacks__stack_in, q._QueueWithStacks__stack_out)
    print(q.deque(), q._QueueWithStacks__stack_in, q._QueueWithStacks__stack_out)

    