from graphviz import Digraph


class Node:

    def __init__(self, type, value=None, left=None, down=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.down = down
        self.right = right

    def to_graphviz(self, graph=None, parent_node=None, edge_label=None, visited=None):
        if not graph:
            graph = Digraph()

        if not visited:
            visited = set()

        if self.value:
            node_id = f'{id(self)}_{self.value}'
            node_label = str(self.value)
        else:
            node_id = f'{id(self)}_{self.type}'
            node_label = self.type

        if node_id not in visited:
            visited.add(node_id)
            graph.node(node_id, label=node_label)

            if parent_node:
                graph.edge(parent_node, node_id, label=edge_label)

            if self.left:
                self.left.to_graphviz(graph, node_id, 'left', visited)

            if self.down:
                self.down.to_graphviz(graph, node_id, 'down', visited)

            if self.right:
                self.right.to_graphviz(graph, node_id, 'right', visited)

        return graph
