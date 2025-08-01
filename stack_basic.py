
# Day 29: Stack Implementation using Python List

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def display(self):
        print("Current Stack:", self.stack)

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top of stack:", s.peek())
print("Popped item:", s.pop())
s.display()
