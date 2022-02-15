def latex_generator_table(in_file, out_file):
    # to write a header of .tex file
    file_header = open('artifacts/utility-files/table_file_header.txt', 'r')
    out_file.write(file_header.read())

    # counts of lines and columns are written in the first line of input line
    cnt_row, cnt_col = in_file.readline().split()
    begin_table = '\\begin{tabular}{||' + int(cnt_col) * ' c |' + '|}\n'

    out_file.write(begin_table)

    # to write a table
    lines = in_file.read().splitlines()
    map = [line.split() for line in lines]

    for line in map:
        str = '\hline \n'
        str += line[0]
        for elem in line[1:]:
            str += ' & ' + elem

        str += ' \\\\ \n'
        out_file.write(str)

    end_table = open('artifacts/utility-files/table_end_file.txt', 'r')
    out_file.write(end_table.read())
