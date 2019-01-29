#doubly linked list

class Node(object):
    
    def __init__(self, value):

        self._value = value
        self._next_node = None
        self._prev_node = None

class DoublyLinkedList(object):

    def __init__(self):
        
        self._head = None
        self._tail = None
        self._size = 0


    def insert_at_head(self, value):
        
        new_node = Node(value)

        if self._head == None:
            self._head = new_node
            self._tail = new_node
            new_node._next_node = None
            new_node._prev_node = None
        else:
            old_head = self._head
            self._head = new_node
            new_node._next_node = old_head
            old_head._prev_node = new_node
        self._size += 1

    
    def insert_at_tail(self, value):
        
        new_node = Node(value)

        if self._head == None:
            self._head = new_node
            self._tail = new_node
            new_node._next_node = None
            new_node._prev_node = None
        else:
            old_tail = self._tail
            self._tail = new_node
            old_tail._next_node = new_node
            new_node._prev_node = old_tail
            new_node._next_node = None
        self._size += 1


    def insert_before_node(self, node, value):
        
        new_node = Node(value)

        if node == None:
            return None
        if self._head == node:
            self._head = new_node
            node._prev_node = new_node
            new_node._next_node = node        
        else:
            new_node._prev_node = node._prev_node
            node._prev_node._next_node = new_node
            new_node._next_node = node
            node._prev_node = new_node
        self._size += 1

    def insert_after_node(self, node, value):

        new_node = Node(value)

        if node == None:
            return None
        new_node._prev_node = node
        new_node._next_node = node._next_node
        node._next_node._prev_node = new_node
        node._next_node = new_node
        self._size += 1


    def remove_node(self, node):
        
        if node == None:
            return None
        if self._tail == node:
            node._prev_node._next_node = None
            self._tail = node._prev_node
        elif self._head == node:
            self._head = node._next_node
            node._next_node._prev_node = None
        else:
            node._prev_node._next_node = node._next_node
            node._next_node._prev_node = node._prev_node
        self._size -= 1


    def remove_head(self):
        
        if self._head == None:
            print('Cannot remove from empty list')
            return None
        node = self._head
        self._head = node._next_node
        node._next_node._prev_node = None
        self._size -= 1

    
    def remove_tail(self):
        
        if self._head == None:
            print('Cannot remove from empty list')
            return None
        node = self._tail
        self._tail = node._prev_node
        node._prev_node._next_node = None
        self._size -= 1


    def get_nth_node(self, n):
        
        node = self._head
        for i in range(1, n):
            if node._next_node != None:
                node = node._next_node
            else:
                break
        if node._next_node != None:
            return node._value
        else:
            return None


    def get_size(self):

        return self._size
        #size = 0
        #node = self._head
        #while node != None:
        #    size += 1
        #    node = node._next_node
        #return size


    def print_list(self):

        node = self._head
        while node != None:
            print(node._value)
            node = node._next_node


    def reverse_list(self):

        node = self._head
        if node == None:
            return None
        for i in range(self._size):
            while node._next_node != None:
                if node._value < node._next_node._value:
                    temp = node._value
                    node._value = node._next_node._value
                    node._next_node._value = temp
                node = node._next_node
            node = self._head


    def sort_list(self):
        
        node = self._head
        if node == None:
            return None
        for i in range(self._size):
            while node._next_node != None:
                if node._value > node._next_node._value:
                    temp = node._value
                    node._value = node._next_node._value
                    node._next_node._value = temp
                node = node._next_node
            node = self._head


    def search_list(self, target):
        
        node = self._head
        while node != None and node._value != target:
            if node._value == target:
                break
            node = node._next_node
        if node == self._head and node._value != target:
            return None
        return node

    
d_list = DoublyLinkedList()
d_list.insert_at_head(5)
d_list.insert_at_head(3)
d_list.insert_at_tail(8)
#d_list.print_list()
node = d_list.search_list(5)
d_list.insert_before_node(node, 6)
d_list.insert_after_node(node, 19)
d_list.insert_after_node(node, 4)
#d_list.print_list()
d_list.remove_node(node)
d_list.print_list()
print()
#d_list.remove_head()
#d_list.remove_tail()
d_list.print_list()
print('Head: ', d_list._head._value)
print('Tail: ', d_list._tail._value)
print('2nd node: ', d_list.get_nth_node(2))
print('3rd node: ', d_list.get_nth_node(3))
print('8th node: ', d_list.get_nth_node(8))
print()
print()
d_list.insert_at_head(11)
d_list.print_list()
d_list.sort_list()
print('Sorted: ')
d_list.print_list()
print('Reversed: ')
d_list.reverse_list()
d_list.print_list()
