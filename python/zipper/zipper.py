class Zipper:
    def __init__(self, tree, past):
        self.tree = tree
        self.past = past
        
    def from_tree(tree):
        '''get a zipper out of a tree, the focus is on the root node'''
        return Zipper(tree, [])

    def value(self):
        '''get the value of the focus node'''
        return self.tree['value']

    def set_value(self, value):
        '''set the value of the focus node, returns a new zipper'''
        self.tree['value'] = value
        return self

    def left(self):
        if not self.tree['left']:
            return None
        return Zipper(self.tree['left'], self.past + [self.tree])

    def set_left(self, tree):
        self.tree['left'] = tree
        return self

    def right(self):
        if not self.tree['right']:
            return None
        return Zipper(self.tree['right'], self.past + [self.tree])

    def set_right(self, tree):
        self.tree['right'] = tree
        return self

    def up(self):
        '''move the focus to the parent, returns a new zipper'''
        return Zipper(self.past[-1], self.past)

    def to_tree(self):
        '''get the tree out of the zipper'''
        if self.past:
            return self.past[0]
        return self.tree
