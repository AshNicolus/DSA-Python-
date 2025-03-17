from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node: Optional[TreeNode], current_path: str, result: List[str]):
            if not node:
                return
            new_path = current_path + str(node.val)
            
            if not node.left and not node.right:
                result.append(new_path)
                return
            
    
            new_path += "->"
            dfs(node.left, new_path, result)
            dfs(node.right, new_path, result)
        
        result = []
        if root:
            dfs(root, "", result)
        return result
