# Problem B

class Queue:
    """A queue datatype."""

    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)
        return self.data

    def dequeue(self):
        return self.data.pop(0)

    def is_empty(self):
        return not self.data
    
    
# Problem C

class Node:
    """A node datatype."""

    def __init__(self, value):
        self.data = value
        self.next = None