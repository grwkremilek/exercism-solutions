class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        out = 'TreeNode(data={}, left={}, right={})'
        return out.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.node = TreeNode(tree_data[0])
        self.root = TreeNode(tree_data[0])
        self.output = []
        for data in tree_data[1:]:
            self._add(data, self.node)

    def data(self):
        return self.node

    def sorted_data(self):
        self._get_lowest(self.node, self._output_node)
        return self.output
        #return self._traverse_inorder(self.root)
        
    def _add(self, new_data, node):
        if new_data <= node.data:
            if not node.left:
                node.left = TreeNode(new_data)
            else:
                self._add(new_data, node.left)
        else:
            if not node.right:
                node.right = TreeNode(new_data)
            else:
                self._add(new_data, node.right)
    
    def _traverse_inorder(self):
        left = self._traverse_inorder(root.left)
        right = self._traverse_inorder(root.right)
        return left + [node.data] + right
    
    def _get_lowest(self, node, func):
            if node is None:
                return
            else:
                self._get_lowest(node.left, func)
                func(node)
                self._get_lowest(node.right, func)
                
    def _output_node(self, node):
            self.output.append(node.data)
