#!/usr/bin/python
#elements can be added or removemd from the front or the rear

class Deque(object):

    def __init__(self, size=10):
        
        self.size = size
        self._deque = [None] * self.size
        self.front = 0
        self.rear = -1

    def is_empty(self):
        
        return self.rear == -1

    def is_full(self):
            
        if self.rear == self.size - 1:
            print('Deque is full')
            return True
        return False
    
    def expand_deque_size(self):

        self.size *= 2
        temp = self._deque
        self.deque = [None] * self.size
        for i in range(len(temp)):
            self._deque[i] = temp[i]

    def add_front(self, element):
        
        if self.is_empty():
            self._deque[self.front] = element
        else:
            if self.rear == self.size - 2:
                expand_deque_size()
            for i in range(len(self._deque)-2, -1, -1):
                self._deque[i + 1] = self._deque[i]
            self._deque[self.front] = element
        self.rear += 1

    def add_rear(self, element):
        
        self.rear += 1
        if self.is_empty():
            self._deque[self.rear] = element
        else:
            if self.rear == self.size -1:
                expand_deque_size()
            self._deque[self.rear] = element
    
    def remove_front(self):        

        if not self.is_empty():
            deq = self._deque[self.front]
            for i in range(1,len(self._deque)):
                self._deque[i-1] = self._deque[i]
            self.rear -= 1
            return deq
        return None

    def remove_rear(self):
    
        if not self.is_empty():
           deq = self._deque[self.rear]
           self._deque[self.rear] = None
           self.rear -= 1
           return deq
        return None

    def print_deque(self):

        print('Deque: ', end='')
        for e in self._deque:
            if e != None:
                print(e, end=' ')
        print()

dq = Deque()
dq.add_front(5)
dq.add_front(3)
dq.add_rear(7)
dq.add_rear(9)
dq.print_deque()
dq.remove_front()
dq.print_deque()
dq.remove_rear()
dq.print_deque()
dq.remove_rear()
dq.print_deque()
dq.remove_rear()
dq.print_deque()
dq.remove_rear()
dq.print_deque()
