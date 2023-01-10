# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 09:03:38 2022

@author:  https://favtutor.com/blogs/tree-traversal-python-with-recursion
"""

class TreeNode:
    def __init__(self, val):
        self.nodeData = val
        self.left = None
        self.right = None


def inorderTraversalUtil(root, answer):
    if root is None:
        return
    inorderTraversalUtil(root.left, answer)
    answer.append(root.nodeData)
    inorderTraversalUtil(root.right, answer)
    return

def postorderTraversalUtil(root, answer):
    if root is None:
        return
    postorderTraversalUtil(root.left, answer)
    postorderTraversalUtil(root.right, answer)
    answer.append(root.nodeData)
    return


    return

def preorderTraversalUtil(root, answer):
    if root is None:
        return
    
    answer.append(root.nodeData)
    preorderTraversalUtil(root.left, answer)
    preorderTraversalUtil(root.right, answer)

    return

myTree ='''
Build the following tree
                 1
               /   \\
              2     3
            /  \\  
           4   5

'''

print(myTree)
root = TreeNode(1)
root = TreeNode("1")
root.left = TreeNode("2")
root.right = TreeNode("3")
root.left.left = TreeNode("4")
root.left.right = TreeNode("5")
root.left.right.left = TreeNode("6")
    

inOrder_list = []
inorderTraversalUtil(root, inOrder_list)
print("in-order",inOrder_list)

postOrder_list = []
postorderTraversalUtil(root, postOrder_list)
print("post-order",postOrder_list)

preOrder_list = []
preorderTraversalUtil(root, preOrder_list)
print("pre-order", preOrder_list)

from subTree_display import *
t = ShowTree_ADT()
t.displayNodes5G(root)  







