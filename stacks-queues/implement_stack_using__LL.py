class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None  # Initialize the stack with an empty head

    # Function to push an integer onto the stack
    def push(self, data):
        new_node = StackNode(data)  # Create a new node with the data
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node

    # Function to remove an item from the top of the stack
    def pop(self):
        if self.head is None:  # If the stack is empty
            return -1  # Return -1 as per the problem statement
        popped_data = self.head.data  # Get the data at the head
        self.head = self.head.next  # Move the head to the next node
        return popped_data  # Return the popped data
