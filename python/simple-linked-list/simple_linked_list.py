class Node:    
    def __init__(self, value):
        self._value = value
        self._next = None
        
    def value(self):
        return self._value
        
    def next(self):
        return self._next


class LinkedListIterator:
    def __init__(self, linked_list):
        self._current = linked_list._head
    
    def _reset_iteration(self):
        self._current = self._head
        
    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = self._current.value()
        self._current = self._current.next()
        return value    


class LinkedList:
    def __init__(self, values = []):
        self._values = values
        self._head = None
        self._next = None
        self._len = 0
        [self.push(value) for value in values]

    def __len__(self):
        return self._len
  
    def __iter__(self):
        return LinkedListIterator(self)
 
    def push(self, value):
        new_node = Node(value)
        new_node._next, self._head = self._head, new_node
        self._len += 1
 
    def pop(self, value=None):
        if self._head is None:
            raise EmptyListException()
        v, self._head = self._head.value(), self._head._next
        self._len -= 1
        return v

    def head(self):
        if self._len == 0:
            raise EmptyListException()
        return self._head

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    def __init__(self):
            self.message = "Linked list is empty"
            
    def __str__(self):
        return repr(self.message)
