from json import dumps


class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def _find_node(self, label):
        if (self.label == label):
            return self
        for node in self.children:
            reparented = node._find_node(label)
            if reparented:
                self.children.remove(node)
                node.children = [self] + node.children
                return reparented
    
    def _transverse(self, label):
        if (self.label == label):
            return [self.label]
        for node in self.children:
            labels = node._transverse(label)
            if (labels):
                return [self.label] + labels

    def from_pov(self, from_node):
        out = self._find_node(from_node)
        if not out:
            raise ValueError ("Invalid input.")
        return out

    def path_to(self, from_node, to_node):
        reparented = self.from_pov(from_node)
        out = reparented._transverse(to_node)
        if not out:
            raise ValueError ("Invalid input.")
        return out

