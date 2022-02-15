from latex_generator import latex_generator_table


def main():
    in_file = open('artifacts/input.txt', 'r')
    out_file = open('artifacts/output.tex', 'w')
    latex_generator_table(in_file, out_file)


if __name__ == '__main__':
    main()