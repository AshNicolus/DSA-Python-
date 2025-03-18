from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxpath(node):
            if node is None:
                return 0 
            left_sum = max(maxpath(node.left),0)
            right_sum = max(maxpath(node.right),0)
            self.maxi = max(self.maxi,left_sum+right_sum+node.val)
            return node.val + max(left_sum,right_sum)
        self.maxi = float('-inf')
        maxpath(root)
        return self.maxi