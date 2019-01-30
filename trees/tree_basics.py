#!/usr/bin/env python3
#trees

#tree has a root (at the top), branches and leaves(grow downwards)
#all children of one node are independent of the children of another node
#each leaf node is unique

#each node has a name (key) and other info (payload)

#edge connects two nodes
#every node (except root) is connected by exactly one incoming edge from another node
#each node may have several outgoing edges

#path is an ordered list of nodes connected by edges

#children are sets of nodes that have incoming edges
#a node is the parent of all the nodes it connects to with outgoing edges
#siblings are children of the same parent node
#subtree is a set of nodes and edges comprised of a parent and all descendents of the parent
#leaf node is a node without children

#level is the number of edges on the path from the root node
#height is how many levels are in the tree

#if each node in the tree has a max of two children, its a binary tree


##implementation using list of lists
#1st element will be root node
#2nd element will be a list that represents the left subtree
#3rd element will be a list that represents the right subtree

def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):

    #get left branch
    t = root.pop(1)

    #if t has children
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    #if branch is empty
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):

    #get right branch
    t = root.pop(2)

    #if t has children
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    #if branch is empty
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root(root):
    return root[0]

def set_root(root, value):
    root[0] = value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

r = binary_tree(3)
insert_left(r, 4)
insert_right(r, 6)
insert_right(r, 7)
left = get_left_child(r)
right = get_right_child(r)
set_root(r, 1)
print('root: ', r)
print('left branch: ', left)
print('right branch: ', right)
