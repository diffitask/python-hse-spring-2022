import networkx as nx
import ast
import matplotlib.pyplot as plt
import ast_tree

f = open('fibonacci_func.py', 'r')
ast_object = ast.parse(f.read())

#print(ast.dump(ast_object))
#print(ast_object._fields)
# print(ast.unparse(ast_object))

G = nx.Graph()
graph = ast_tree.AstGraph()
graph.dfs_graph(G, ast_object)
plt.figure(0, (10, 10))
nx.draw(G,
        nx.drawing.nx_agraph.graphviz_layout(G, prog="dot"),
        with_labels=True,
        labels=graph.labels_list)
plt.show()
