class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        # Copy the value from the next node to the current node
        node.val = node.next.val
        # Bypass the next node
        node.next = node.next.next