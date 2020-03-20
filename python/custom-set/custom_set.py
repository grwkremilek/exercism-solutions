class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements = []
        for element in elements:
            self.add(element)

    def isempty(self):
        return self.elements == []

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return set(self.elements).issubset(set(other.elements))

    def isdisjoint(self, other):
        return set(self.elements).isdisjoint(set(other.elements))

    def __eq__(self, other):
        return set(self.elements) == set(other.elements)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        res = [e for e in self.elements if e in other.elements]
        return CustomSet(res)

    def __sub__(self, other):
        res = [e for e in self.elements if e not in other.elements]
        return CustomSet(res)

    def __add__(self, other):
        res = CustomSet(self.elements)
        for element in other.elements:
            res.add(element)
        return res
