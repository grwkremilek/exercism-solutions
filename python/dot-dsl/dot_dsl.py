NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        
        if not isinstance(data, list):
            raise TypeError("Incorrect input type")
        
        for tpl in data:
            if len(tpl) < 2:
                raise TypeError('This is a silly exception')
            
            if tpl[0] == 0:
                if not isinstance(tpl[1], str) or not isinstance(tpl[2], dict):
                    raise ValueError("Incorrect input types")
                self.nodes.append(Node(tpl[1], tpl[2]))
            elif tpl[0] == 1:
                if not isinstance(tpl[1], str) or not isinstance(tpl[2], str) or not isinstance(tpl[3], dict):
                    raise ValueError("Incorrect input types")
                self.edges.append(Edge(tpl[1], tpl[2], tpl[3]))
            elif tpl[0] == 2:
                if not isinstance(tpl[1], str) or not isinstance(tpl[2], str):
                    raise ValueError("Incorrect input types")
                self.attrs[tpl[1]] = tpl[2]
            else:
                raise ValueError("Graph expects a list!")
