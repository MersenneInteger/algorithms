#singly linked lists

class Node(object):
    
    def __init__(self, value):

        self._value = value
        self._next_node = None


class SinglyLinkedList(object):

    def __init__(self):
        
        self._head = None
        self._tail = None
        self._size = 0
    
    def insert_node_at_head(self, value):
        
        new_node = Node(value)
        #if list is empty, make new_node head and tail
        if self._head == None:
            self._head = new_node
            self._tail = new_node
            new_node._next_node = None
        else:
            #point new_node to old head and make new_node head
            old_head = self._head
            self._head = new_node
            new_node._next_node = old_head
        self._size += 1

    
    def insert_node_at_tail(self, value):
        
        #make old_tail point to new_node
        new_node = Node(value)
        old_tail = self._tail
        self._tail = new_node
        old_tail._next_node = new_node
        #point new_node to None
        new_node._next_node = None
        self._size += 1

    def remove_node_at_head(self):
        
        if self._head == None:
            print('cannot remove node from an empty list')
            return None
        #point head to None and make next_node the new head
        new_head = self._head._next_node
        self._head._next_node = None
        self._head = new_head
        self._size -= 1

    def remove_node_at_tail(self):
        
        #traverse list to find tail
        if self._head == None:
            print('cannot remove node from an empty list')
            return None
        #start at head, traverse list until find 2nd to last node
        node = self._head
        while node._next_node._next_node != None:
            node = node._next_node
        #point 2nd to last node's next_node to None, making it the tail
        node._next_node = None
        self._tail = node
        self._size -= 1


#    def get_size(self):
#        
#        size = 0
#        node = self._head
#        while node != None:
#            size += 1
#            node = node._next_node
#        return size


    def print_list(self):

        node = self._head
        while node != None:
            print(node._value)
            node = node._next_node

    
    def search_list(self, target):

        node = self._head
        while node != None and node._value != target:
            if node._value == target:
                break
            node = node._next_node
        if node == self._head and node._value != target:
            return None
        return node


llist = SinglyLinkedList()
llist.insert_node_at_head(1)
llist.insert_node_at_head(2)
llist.insert_node_at_head(5)
llist.insert_node_at_tail(7)
llist.insert_node_at_tail(55)
llist.print_list()
print('removing tail')
llist.remove_node_at_tail()
llist.print_list()
print('size of list: ', llist._size)
print('removing head of list')
llist.remove_node_at_head()
llist.print_list()

#search list
find = 1
found_node = llist.search_list(find)
if found_node != None:
    print('Value: ', found_node._value)
    if found_node._next_node != None:
        print('Next node: ', found_node._next_node._value)
    else:
        print(f'node with value {find} is the tail, there is no next node')
else:
    print('Value not found in linked list')
