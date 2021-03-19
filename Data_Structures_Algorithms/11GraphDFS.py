class Node():
    def __init__(self,value):
        self.value = value
        self.adjacent_list = []
        self.visited = False

class Graph():
    def DFS(self,node,traversal):
        node.visited = True
        traversal.append(node.value)

        for element in node.adjacent_list:
            if element.visited is False:
                self.DFS(element,traversal)

        return traversal


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')
node6 = Node('f')
node7 = Node('g')

node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)

node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)

node4.adjacent_list.append(node7)

graph = Graph()
print(graph.DFS(node1,[]))

