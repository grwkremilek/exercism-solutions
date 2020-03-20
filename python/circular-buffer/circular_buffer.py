class BufferFullException(Exception):
    def __init__(self):
            self.message = "The buffer is full."
    
    def __str__(self):
        return repr(self.message)


class BufferEmptyException(Exception):
    def __init__(self):
            self.message = "The buffer is empty."
            
    def __str__(self):
        return repr(self.message)


class CircularBuffer(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException()
        return self.buffer.pop(0)

    def write(self, data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException()
        return self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(data)
        
    def clear(self):
        self.buffer = []
