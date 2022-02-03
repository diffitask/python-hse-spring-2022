import ast
import networkx as nx
import matplotlib.pyplot as plt


class AstGraph:
    G = nx.Graph()
    node_cnt = 0
    labels_list = {}
    colors_list = []
    sizes_list = []

    colors_dict = {'Constant': 'lightblue',
                   'id': 'tan',
                   'ctx': 'pink',
                   'list': 'greenyellow',
                   'default': 'orange'}

    def __init__(self, ast_object):
        self.ast_obj = ast_object

        self.G.add_node(0)
        self.labels_list[0] = self.get_name(ast_object)
        self.sizes_list.append(len(self.get_name(ast_object)) ** 2 * 20 + 100)
        self.colors_list.append(self.colors_dict['default'])
        self.node_cnt += 1

        self.dfs_graph(self.ast_obj, 0)

    def get_name(self, node):
        return node.__class__.__name__

    def set_color(self, node, node_field='default'):
        # possible field names
        if (node_field == 'id' or node_field == 'ctx' or node_field == 'list'):
            pass
        elif (self.get_name(node) == 'Constant'):
            node_field = 'Constant'
        else:
            node_field = 'default'
        self.colors_list.append(self.colors_dict[node_field])

    def make_node(self, node, parent_num, label='', node_type='default'):
        cur_num = self.node_cnt
        self.node_cnt += 1
        self.G.add_node(cur_num)
        self.G.add_edge(parent_num, cur_num)

        self.labels_list[cur_num] = label
        self.sizes_list.append(15 * 5 * 15 + 300)
        self.set_color(node, node_type)
        return cur_num

    def dfs_graph(self, node, node_num):
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                if len(value) > 0:
                    cur_num1 = self.make_node(value, node_num, field, 'list')
                    for elem in value:
                        cur_num2 = self.make_node(elem, cur_num1, self.get_name(elem))
                        self.dfs_graph(elem, cur_num2)

            elif isinstance(value, str):
                self.make_node(value, node_num, field + ' ' + value, field)

            elif isinstance(value, ast.AST):
                cur_num1 = self.make_node(value, node_num, field + ' ' + self.get_name(value), field)
                self.dfs_graph(value, cur_num1)

    def draw_graph(self):
        plt.figure(0, (20, 20))
        nx.draw(self.G,
                nx.drawing.nx_agraph.graphviz_layout(self.G, prog="dot"),
                with_labels=True,
                labels=self.labels_list,
                node_shape='s',
                font_size=9,
                node_color=self.colors_list,
                node_size=self.sizes_list)
        # plt.show()
        plt.savefig("artifacts/graph.png")
