import ast
import networkx as nx
import matplotlib.pyplot as plt


class AstGraph:
    def __init__(self):
        self.G = nx.Graph()
        self.node_cnt = 0
        self.labels_list = {}

    def dfs_graph(self, node):
        self.G.add_node(self.node_cnt)
        self.labels_list[self.node_cnt] = ast.unparse(node)
        cur_num = self.node_cnt
        self.node_cnt += 1

        for ch in ast.iter_child_nodes(node):
            self.G.add_edge(cur_num, self.dfs_graph(ch))
        return cur_num

    def draw_graph(self):
        plt.figure(0, (10, 10))
        nx.draw(self.G,
                nx.drawing.nx_agraph.graphviz_layout(self.G, prog="dot"),
                with_labels=True,
                labels=self.labels_list)
        plt.show()