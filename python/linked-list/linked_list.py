class Node:
    def __init__(self, value, nxt=None, prv=None):
        self.value = value
        self.next = nxt
        self.prev = prv

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def pop(self):
        node = self.tail
        if node is None or node.prev is None:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return node.value

    def shift(self):
        node = self.head
        if node is None or node.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return node.value

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def __len__(self):
        return self.count