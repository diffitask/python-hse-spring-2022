import numpy as np
import numpy.random

from MatrixUser import MatrixUser as MatrixUser

def easy_test():
    numpy.random.seed(0)
    m1 = MatrixUser(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixUser(np.random.randint(0, 10, (10, 10)))

    m_add = m1 + m2
    m_mul = m1 * m2
    m_matmul = m1 @ m2

    with open("artifacts/1-easy/matrix+.txt", "w") as f:
        f.write(m_add.__str__())
    with open("artifacts/1-easy/matrix*.txt", "w") as f:
        f.write(m_mul.__str__())
    with open("artifacts/1-easy/matrix@.txt", "w") as f:
        f.write(m_matmul.__str__())

def main():
    easy_test()

if __name__ == '__main__':
    main()