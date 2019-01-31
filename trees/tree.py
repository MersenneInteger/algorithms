#!/usr/bin/env python3

#tree implementation
class BinaryTree(object):

    def __init__(self, root):

        self._root = root
        self._left_child = None
        self._right_child = None
    

    def insert_left_child(self, node):
        
        if self._left_child == None:
            #when no left child exists
            self._left_child = BinaryTree(node)
        else:
            #there exists a current left child
            t = BinaryTree(node)
            #make current left child the left child of new node
            #push current left child down one level in tree
            t._left_child = self._left_child
            self._left_child = t


    def insert_right_child(self, node):

        if self._right_child == None:
            self._right_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t._right_child = self._right_child
            self._right_child = t


    def get_root(self):

        return self._root


    def set_root(self, value):

        self._root = value


    def get_left_child(self):
        
        return self._left_child
    

    def get_right_child(self):
        
        return self._right_child


if __name__ == '__main__':

    tree = BinaryTree(3)
    tree.insert_left_child(2)
    tree.insert_left_child(6)
    tree.insert_right_child(5)
    tree.insert_right_child(9)
    left = tree.get_left_child()
    right = tree.get_right_child()
    left.insert_right_child(0)
    right.insert_left_child(0)

