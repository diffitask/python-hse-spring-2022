import ast
import networkx as nx
import matplotlib.pyplot as plt


class AstGraph:
    G = nx.Graph()
    node_cnt = 0
    labels_list = {}

    def __init__(self, ast_object):
        self.ast_obj = ast_object

        self.G.add_node(0)
        self.labels_list[0] = self.get_name(ast_object)
        self.node_cnt += 1

        self.dfs_graph(self.ast_obj, 0)

    def get_name(self, node):
        return node.__class__.__name__

    def make_node(self, parent_num, label=""):
        cur_num = self.node_cnt
        self.node_cnt += 1
        self.G.add_node(cur_num)
        self.G.add_edge(parent_num, cur_num)
        self.labels_list[cur_num] = label
        return cur_num

    def dfs_graph(self, node, node_num):
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                if len(value) > 0:
                    cur_num1 = self.make_node(node_num, field)
                    for elem in value:
                        cur_num2 = self.make_node(cur_num1, self.get_name(elem))
                        self.dfs_graph(elem, cur_num2)

            elif isinstance(value, str):
                self.make_node(node_num, field + ' ' + value)

            elif isinstance(value, ast.AST):
                cur_num1 = self.make_node(node_num, field + self.get_name(value))
                self.dfs_graph(value, cur_num1)

    def draw_graph(self):
        plt.figure(0, (10, 10))
        nx.draw(self.G,
                nx.drawing.nx_agraph.graphviz_layout(self.G, prog="dot"),
                with_labels=True,
                labels=self.labels_list)
        # plt.show()
        plt.savefig("artifacts/graph.png")
