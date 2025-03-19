# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder:
            return None  

        root = Node(preorder[0])

   
        root_pos = inorder.index(preorder[0])

   
        root.left = self.buildTree(inorder[:root_pos], preorder[1:root_pos+1])
        root.right = self.buildTree(inorder[root_pos+1:], preorder[root_pos+1:])

        return root
