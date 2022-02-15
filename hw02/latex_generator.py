from functools import reduce


def create_file_epilogue() -> str:
    file_header = open('artifacts/utility-files/latex_file_header.txt', 'r')
    return file_header.read()


def create_table_header(in_file) -> str:
    # counts of lines and columns are written in the first line of input file
    _, cnt_col = in_file.readline().split()
    begin_table = '\\begin{tabular}{||' + int(cnt_col) * ' c |' + '|}\n'
    return begin_table


def create_table_data(file_lines: list[str]) -> str:
    table_lines = map(str.split, file_lines)

    table_lines_str = map(lambda line: '\\hline \n' + reduce(lambda ln, symb: ln + ' & ' + symb, line) + ' \\\\ \n', table_lines)

    table_str = reduce(lambda string, line: string + line,
                       table_lines_str)
    return table_str


def create_table_prologue() -> str:
    return '\\hline \n' + '\\end{tabular} \\\\ \n'


def create_file_prologue() -> str:
    return '\\end{document}'


def latex_file_generator(in_file, out_file):
    out_file.write(create_file_epilogue())
    out_file.write(create_table_header(in_file))

    file_lines = in_file.read().splitlines()
    out_file.write(create_table_data(file_lines))

    out_file.write(create_table_prologue())
    out_file.write(create_file_prologue())
