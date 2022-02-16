import ast
from ast_fibonacci_generator import ast_tree


def main():
    # create ast from file
    f = open('fibonacci_func.py', 'r')
    ast_object = ast.parse(f.read())

    # create graph
    ast_graph = ast_tree.AstGraph(ast_object)
    ast_graph.draw_graph()


if __name__ == '__main__':
    main()
