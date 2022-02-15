import os
from latex_generator import latex_file_generator


def main():
    if not os.path.exists("artifacts"):
        os.mkdir("artifacts")

    in_file = open('artifacts/table_file.txt', 'r')
    out_file = open('artifacts/output.txt', 'w')
    latex_file_generator(in_file, out_file)


if __name__ == '__main__':
    main()
