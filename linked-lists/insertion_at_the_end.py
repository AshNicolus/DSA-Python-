    
class Node:
    def __init__(self,data,next1=None):
        self.data=data
        self.next=next1

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        new_node = Node(x)
        if head is None:
            return new_node
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head
        
        

