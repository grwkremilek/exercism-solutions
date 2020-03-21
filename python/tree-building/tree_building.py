class Record:
    def __init__(self, id_number, parent_id_number):
        self.id = id_number
        self.parent_id = parent_id_number
  

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []
        
    def add_child(self, node):
        self.children.append(node)


def BuildTree(records):
    if not records: return
    records.sort(key=lambda record: record.id)
    if records[0].id != 0 or records[0].parent_id != 0:
        raise ValueError('Incorrect root values')
    if records[-1].id != len(records)-1:
        raise ValueError('Values not continuous')
    root = Node(records[0].id)
    nodes = {records[0].id  : root}
    for rec in records[1:]:
        if rec.parent_id not in nodes:
            raise ValueError('Values in cycle')
        parent = nodes[rec.parent_id]
        node = Node(rec.id)
        parent.add_child(node)
        nodes[rec.id] = node
    return root

