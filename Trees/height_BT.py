from collections import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0 
        
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
