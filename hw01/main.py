import ast
from ast_tree import AstGraph


def main():
    # create ast from file
    f = open('fibonacci_func.py', 'r')
    ast_object = ast.parse(f.read())

    # create graph
    ast_graph = AstGraph()
    ast_graph.dfs_graph(ast_object)
    ast_graph.draw_graph()


if __name__ == '__main__':
    main()
