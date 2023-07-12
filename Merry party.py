class Node:
    def __init__(self, value):
        self.values = {'key': value, 'plus': 0, 'minus': 0, 'OPT': 0}
        self.children = []

    def isLeaf(self):
        return len(self.children) == 0


def dfs(node):
    if node.isLeaf():
        node.values['minus'] = 0
        node.values['OPT'] = node.values['plus']
        print(node.values)
        return

    for child in node.children:
        dfs(child)
        node.values['plus'] += child.values['minus']
        node.values['minus'] += child.values['OPT']
    node.values['OPT'] = max(node.values['plus'], node.values['minus'])
    print(node.values, node.isLeaf(), node.values['plus'], node.values['minus'])


# Create nodes
nodes = [Node(i) for i in range(0, 9)]

nodes[0].values['plus'] = 100
nodes[1].values['plus'] = 60
nodes[2].values['plus'] = 80
nodes[3].values['plus'] = 30
nodes[4].values['plus'] = 200
nodes[5].values['plus'] = 80
nodes[6].values['plus'] = 70
nodes[7].values['plus'] = 40
nodes[8].values['plus'] = 50

# Build the tree
nodes[0].children = [nodes[1], nodes[2]]
nodes[1].children = [nodes[3], nodes[4], nodes[5]]
nodes[3].children = [nodes[6]]
nodes[5].children = [nodes[7], nodes[8]]


# Calculate the maximum number of nodes in a maximally independent set
print("Postorder recursive:")
dfs(nodes[0])
print()
print("Max Independent Set Tree is", nodes[0].values['OPT'])


