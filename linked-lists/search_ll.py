class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, n, head, key):
        #Code here
        while head is not None:
             if head.data == key:
                return True 
                head = head.next
        return False
        
        