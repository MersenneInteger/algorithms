#!/usr/bin/python

#base: bottom of stack, have been in stack the longest
#LIFO: last in, first out
#top: end of stack

class Stack(object):
    
    def __init__(self, size=10):
        
        self.size = size
        self._stack = [None] * size
        self.top = -1

    def push(self, elem):
        
        self.top += 1
        self._stack[self.top] = elem
        if self.top == self.size -1:
            self.size *= 2
            temp = self._stack
            self._stack = [None] * self.size
            for i in range(len(temp)):
                self._stack[i] = temp[i]

    def pop(self):
        
        if self.top == -1:
            print('Error: Popping from an empty stack')
            return None
        popped = self._stack[self.top]
        self._stack[self.top] = None
        self.top -= 1
        return popped
        
    def peek(self):

        return self._stack[self.top]

    def print_stack(self):

        print('Stack: ', end='')
        for e in self._stack:
            if e != None:
                print(e, end=' ')
    
    def get_size(self):

        stack_size = 0
        for e in self._stack:
            if e != None:
                stack_size += 1
        return stack_size
'''
s = Stack()
s.push(5)
for i in range(9):
    s.push(i)
s.print_stack()
print('\npeeking: {}'.format(s.peek()))
s.push(3)
s.print_stack()
print('\npeeking: {}'.format(s.peek()))
p = s.pop()
print('popped: {}'.format(p))
s.print_stack()
p = s.pop()
print('\npopped: {}'.format(p))
s.print_stack()
for i in range(1,9):
    s.push(i)
print('')
s.print_stack()
'''
