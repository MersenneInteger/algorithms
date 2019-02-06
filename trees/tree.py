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

    ##inorder traversal
    #recursively do traversal of left subtree, visit root then visit right subtree
    def inorder_traverse(self):

        if self._left_child:
            self._left_child.inorder_traverse()
        print(self._root)
        if self._right_child:
            self._right_child.inorder_traverse()

    ##preorder traversal
    #root -> left -> right
    def preorder_traverse(self):

        print(self._root)
        if self._left_child:
            self._left_child.preorder_traverse()
        if self._right_child:
            self._right_child.preorder_traverse()    

    ##postorder traversal
    #recursively traverse left, then right then root
    def postorder_traverse(self):

        if self._left_child:
            self._left_child.postorder_traverse()
        if self._right_child:
            self._right_child.postorder_traverse()
        print(self._root)


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

    print('Inorder traversal')
    tree.inorder_traverse()

    print('Preorder traversal')
    tree.preorder_traverse()

    print('Postorder traversal')
    tree.postorder_traverse()

    print('left and right children')
    print(tree._left_child._root)
    print(tree._right_child._root)

