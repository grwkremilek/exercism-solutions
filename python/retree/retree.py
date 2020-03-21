def create_node(v = None, left = {}, right = {}):
    node = {}
    if v:
        keys = ["v", "l", "r"]
        node["v"] =  v
        node["l"] =  left
        node["r"] =  right
    return node
    
def tree_from_traversals(preorder, inorder): 
    if set(preorder) != set(inorder) or len(preorder) != len(set(preorder)):
        raise ValueError("Incompatible values")
    if not preorder:
        return create_node()
    node = create_node(preorder[0])
    ind = inorder.index(preorder.pop(0))    
    node["l"] = tree_from_traversals(preorder[:ind], inorder[:ind])
    node["r"] = tree_from_traversals(preorder[ind:], inorder[ind+1:])
    return node
