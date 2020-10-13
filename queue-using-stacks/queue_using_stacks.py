# Task
# - Implement a Queue using Stacks

# Example:
# >>> a = Stack()
# >>> a.push(1)
# >>> a.push(2)
# >>> a.push(3)
# >>> a.pop()
#   3
# >>> a.pop()
#   2
# >>> a.pop()
#   1
# >>> a.pop()
#   IndexError: list index out of range

import time

# Solutions copied from https://www.geeksforgeeks.org/queue-using-stacks/

#
# Method 1 classic solution (making enqueue method costly)
#
# enQueue = O(N), deQueue = O(1)
#
# enQueue(q, x):
# While stack1 is not empty, push everything from stack1 to stack2.
# Push x to stack1 (assuming size of stacks is unlimited).
# Push everything back to stack1.
# Here time complexity will be O(n)
#
# deQueue(q):
# If stack1 is empty then error
# Pop an item from stack1 and return it
# Here time complexity will be O(1)
class Method1Queue:  
    def __init__(self): 
        self.s1 = [] 
        self.s2 = [] 
  
    def enQueue(self, x): 
          
        # Move all elements from s1 to s2  
        while len(self.s1) != 0:  
            self.s2.append(self.s1[-1])  
            self.s1.pop() 
  
        # Push item into self.s1  
        self.s1.append(x)  
  
        # Push everything back to s1  
        while len(self.s2) != 0:  
            self.s1.append(self.s2[-1])  
            self.s2.pop() 
  
    # Dequeue an item from the queue  
    def deQueue(self): 
          
            # if first stack is empty  
        if len(self.s1) == 0:  
            print("Q is Empty") 
      
        # Return top of self.s1  
        x = self.s1[-1]  
        self.s1.pop()  
        return x 


# Method 2, making dequeue method costly
#
# enQueue = O(1), deQueue = O(N)
# enQueue(q,  x)
#   1) Push x to stack1 (assuming size of stacks is unlimited).
# Here time complexity will be O(1)
#
# deQueue(q)
#   1) If both stacks are empty then error.
#   2) If stack2 is empty
#        While stack1 is not empty, push everything from stack1 to stack2.
#   3) Pop the element from stack2 and return it.
# Here time complexity will be O(n)
class Method2Queue: 
    def __init__(self): 
        self.s1 = [] 
        self.s2 = [] 
  
    # EnQueue item to the queue 
    def enQueue(self, x): 
        self.s1.append(x) 
  
    # DeQueue item from the queue 
    def deQueue(self): 
  
        # if both the stacks are empty 
        if len(self.s1) == 0 and len(self.s2) == 0: 
            print("Q is Empty") 
            return
  
        # if s2 is empty and s1 has elements 
        elif len(self.s2) == 0 and len(self.s1) > 0: 
            while len(self.s1): 
                temp = self.s1.pop() 
                self.s2.append(temp) 
            return self.s2.pop() 
  
        else: 
            return self.s2.pop() 

# Method 3, implementation of Method 2 using one user stack and one Function Call stack
#
# enQueue(x)
#   1) Push x to stack1.
#
# deQueue:
#   1) If stack1 is empty then error.
#   2) If stack1 has only one element then return it.
#   3) Recursively pop everything from the stack1, store the popped item 
#     in a variable res,  push the res back to stack1 and return res
class Method3Queue: 
    def __init__(self): 
        self.s = [] 
          
    # Enqueue an item to the queue  
    def enQueue(self, data): 
        self.s.append(data) 
          
    # Dequeue an item from the queue  
    def deQueue(self): 
        # Return if queue is empty 
        if len(self.s) <= 0: 
            print('Queue is empty') 
            return
          
        # pop an item from the stack 
        x = self.s[len(self.s) - 1] 
        self.s.pop() 
          
        # if stack become empty 
        # return the popped item 
        if len(self.s) <= 0: 
            return x 
              
        # recursive call 
        item = self.deQueue() 
          
        # push popped item back to 
        # the stack 
        self.s.append(x) 
          
        # return the result of  
        # deQueue() call 
        return item 

# Complexity of these operations?
def meta(q, N):
    for i in range(N):
        q.enQueue(i)

    for i in range(N):
        q.deQueue()

if __name__ == '__main__': 
    N = 500

    print("Using Method 1")
    start = time.time()
    q = Method1Queue() 
    meta(q=q, N=N)
    end = time.time() 
    print(f"Method 1 takes {end - start}")

    print("Using Method 2")
    start = time.time()
    q = Method2Queue() 
    meta(q=q, N=N)
    end = time.time() 
    print(f"Method 2 takes {end - start}")

    print("Using Method 3")
    start = time.time()
    q = Method3Queue() 
    meta(q=q, N=N)
    end = time.time() 
    print(f"Method 3 takes {end - start}")
