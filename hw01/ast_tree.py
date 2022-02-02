import ast
import astunparse

class AstGraph:
    num = 0
    labels_list = {}

    def dfs_graph(self, G, ast_object):
        if isinstance(ast_object, list):
            G.add_node(self.num)
            self.labels_list[self.num] = 'list'

            cur_num = self.num
            self.num += 1
            for i in ast_object:
                G.add_edge(cur_num, self.dfs_graph(G, i))
                self.num += 1
            return cur_num

        elif isinstance(ast_object, ast.AST):
            self.labels_list[self.num] = ast.unparse(ast_object)
            cur_num = self.num
            self.num += 1
            for elem in ast_object._fields:
                attr = ast_object.__getattribute__(elem)
                if attr is not None:
                    G.add_edge(cur_num, self.dfs_graph(G, attr))
            return cur_num
        else:
            self.labels_list[self.num] = str(ast_object)
            cur_num = self.num
            self.num += 1
            return cur_num