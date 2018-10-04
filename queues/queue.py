#!/usr/bin/python

#rear: end of queue where new elements are added (queued)
#front: front of the queue, oldest element
#elements start at rear and move toward front
#FIFO: first in, first out

class Queue(object):

    def __init__(self, size=10):
        
        self._queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = -1
    
    def is_empty(self):
        
        return self.rear == -1
    
    def is_full(self):
        
        if self.rear == self.size - 1:
            print('Queue is full')
            return True
        return False

    def enqueue(self, element):
        
        if not self.is_full():
            self.rear += 1
            self._queue[self.rear] = element
        else:
            return None

    def dequeue(self):
        
        deq = self._queue[self.front]
        self._queue[self.front] = None
        if self.rear == self.front:
            self.front = 0
            self.rear = -1
            return None
        else:
            self.front += 1
        print('rear: {0}, front: {1}'.format(self.rear, self.front))
        return deq

    def peek(self):
        
        if not self.is_empty():
            return self._queue[self.rear]

    def print_queue(self):
        
        print('Queue: ', end='')
        if self.is_empty():
            print('Queue is empty')
        else:
            for e in self._queue:
                if e != None:
                    print(e, end=' ')

q = Queue()
q.enqueue(5)
q.enqueue(3)
q.print_queue()
q.enqueue(9)
q.enqueue(7)
print()
q.print_queue()
print('\ndequeuing: {}'.format(q.dequeue()))
q.print_queue()
print('\ndequeuing: {}'.format(q.dequeue()))
q.print_queue()
print('\ndequeuing: {}'.format(q.dequeue()))
q.print_queue()
print('\ndequeuing: {}'.format(q.dequeue()))
q.print_queue()
print('\ndequeuing: {}'.format(q.dequeue()))
q.print_queue()

