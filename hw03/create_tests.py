import numpy as np
import numpy.random

from MatrixUser import MatrixUser as MatrixUser

def write_matrix_to_file(file, matrix: MatrixUser):
    with open(file, "w") as f:
        f.write(matrix.__str__())

def easy_test():
    numpy.random.seed(0)
    m1 = MatrixUser(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixUser(np.random.randint(0, 10, (10, 10)))

    m_add = m1 + m2
    m_mul = m1 * m2
    m_matmul = m1 @ m2

    write_matrix_to_file("artifacts/1-easy/matrix+.txt", m_add)
    write_matrix_to_file("artifacts/1-easy/matrix*.txt", m_mul)
    write_matrix_to_file("artifacts/1-easy/matrix@.txt", m_matmul)

def hard_test():
    m_a = MatrixUser([[2, 1], [0, 1]])
    m_c = MatrixUser([[0, 3], [1, 0]])
    m_b = MatrixUser([[2, 1]])
    m_d = MatrixUser([[2, 1]])

    write_matrix_to_file("artifacts/3-hard/A.txt", m_a)
    write_matrix_to_file("artifacts/3-hard/B.txt", m_b)
    write_matrix_to_file("artifacts/3-hard/C.txt", m_c)
    write_matrix_to_file("artifacts/3-hard/D.txt", m_d)

    m_ab = m_a @ m_b
    m_cd = m_c @ m_d

    write_matrix_to_file("artifacts/3-hard/AB.txt", m_ab)
    write_matrix_to_file("artifacts/3-hard/CD.txt", m_cd)

    with open("artifacts/3-hard/hash.txt", "w") as f:
        f.write("Hash AB: " + str(m_ab.__hash__()) + "\n" +
                "Hash CD: " + str(m_cd.__hash__()) + "\n")


def main():
    easy_test()
    hard_test()

if __name__ == '__main__':
    main()