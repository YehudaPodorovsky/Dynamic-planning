class Node:
    def __init__(self, value):
        self.values = {'key': value, 'plus': 0, 'minus': 0, 'OPT': 0}
        self.children = []

    def isLeaf(self):
        return len(self.children) == 0


def dfs(node):
    if node.isLeaf():
        print(node.values)
        node.values['plus'] = 1
        node.values['minus'] = 0
        node.values['OPT'] = 1
        return

    node.values['plus'] += 1
    for child in node.children:
        dfs(child)
        node.values['plus'] += child.values['minus']
        node.values['minus'] += child.values['OPT']

    node.values['OPT'] = max(node.values['plus'], node.values['minus'])
    print(node.values)


# Create nodes
nodes = [Node(i) for i in range(0, 20)]

# Build the tree
nodes[0].children = [nodes[1], nodes[2], nodes[3], nodes[4]]
nodes[1].children = [nodes[5], nodes[6], nodes[7], nodes[8], nodes[9]]
nodes[2].children = [nodes[10]]
nodes[3].children = [nodes[11], nodes[12]]
nodes[4].children = [nodes[13]]
nodes[13].children = [nodes[14], nodes[15], nodes[16], nodes[17], nodes[18], nodes[19]]

# Calculate the maximum number of nodes in a maximally independent set
print("Postorder recursive:")
dfs(nodes[0])
print()
print("Max Independent Set Tree is", nodes[0].values['OPT'])


