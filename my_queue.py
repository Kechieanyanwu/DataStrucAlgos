# designing a custom queue using only two stacks
# Queue is FIFO, first in, first out, but if i'm using a stack, its kinda technically, last in index, first out
    # so if I'm pushing something to the queue, it goes to the first index in the queue!

# Void Push(int x): Pushes element at the end of the queue.
# Int Pop(): Removes and returns the element from the front of the queue.
# Int Peek(): Returns the element at the front of the queue.
# Boolean Empty(): Returns TRUE if the queue is empty. Otherwise FALSE.

# The Pop() and Peek() methods will always be called on non-empty stacks.

# make sure to use the methods on the stacks, not methods of lists!

class My_queue:
    def __init__(self):
        self.queue = Stack() 
    def push(self, x):
        # if there's nothing in the stack, just append
        if self.queue.size() == 0:
            self.queue.push(x)
        else:
            # create a temporary stack
            temp_stack = Stack()
            
            #append existing queue to the temporary stack 
            while not self.queue.size() == 0:
                temp_stack.push(self.queue.pop())   

            # append new item (last in queue) to the empty queue
            self.queue.push(x)

            #append rest of the queue back 
            while not temp_stack.size() == 0:
                self.queue.push(temp_stack.pop())  
            
            return 
    def pop(self):
        return self.queue.pop()
    def peek(self):
        return self.queue.top()
    def empty(self):
        return self.queue.is_empty()
    

class Stack:
    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
    

trial = My_queue()

print(trial.push(1))
print(trial.push(2))
print(trial.push(3))
print(trial.peek())
print(trial.pop())
print(trial.peek())
print(trial.push(4))
print(trial.pop())
print(trial.pop())
print(trial.push(5))
print(trial.peek())
print(trial.empty())