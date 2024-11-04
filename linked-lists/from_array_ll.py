# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def constructLL(self, arr):
        if not arr:
            return None

        # Initialize the head of the linked list
        head = Node(arr[0])
        current = head

        # Loop through the array starting from the second element
        for value in arr[1:]:
            current.next = Node(value)
            current = current.next

        return head

