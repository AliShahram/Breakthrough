class Node (object):
    def __init__(self, state = None):
        self.parent = None
        self.child = []
        self.action = None
        self.state = state
        self.utility = None

    def add_child(self, node):
        self.child.append(node.state)
        node.parent = self

  
    















