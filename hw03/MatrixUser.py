class HashFuncMixin:
    def count_239_hash(self):
        # sum of 3rd deg of the first elements of each row, and * 239
        return 239 * sum(row[0] * row[0] * row[0] for row in self._matrix)


class MatrixUser(HashFuncMixin):
    _cache_map = {}

    def __init__(self, elements):
        self._row_cnt = len(elements)
        self._col_cnt = len(elements[0])
        self._matrix = []

        for row in elements:
            # incorrect size of a given array
            if len(row) != self._col_cnt:
                raise Exception("Wrong row size of a given data array\n")
            self._matrix.append(row)

    def __str__(self) -> str:
        s = ""
        for row in self._matrix:
            s += row.__str__() + "\n"
        return s

    def __hash__(self):
        return self.count_239_hash()

    def _check_types(self, other):
        # checking the class of the other matrix
        if not (isinstance(other, MatrixUser)):
            raise Exception("Other matrix doesn't belong to the class MatrixUser")

    def _check_sizes(self, other):
        # checking the sizes of matrices
        if not (self._row_cnt == other._row_cnt and self._col_cnt == other._col_cnt):
            raise Exception("Operation is impossible -- matrices have different sizes: "
                            + str(self._row_cnt) + " " + str(self._col_cnt) + "versus"
                            + str(other._row_cnt) + " " + str(other._col_cnt))

    def __eq__(self, other):
        self._check_types(other)
        return self._matrix == other._matrix

    def __add__(self, other):
        self._check_types(other)
        self._check_sizes(other)
        return MatrixUser([[self._matrix[i][j] + other._matrix[i][j]
                        for j in range(self._row_cnt)]
                        for i in range(self._col_cnt)])

    def __mul__(self, other):
        self._check_types(other)
        self._check_sizes(other)
        return MatrixUser([[self._matrix[i][j] * other._matrix[i][j]
                        for j in range(self._row_cnt)]
                        for i in range(self._col_cnt)])

    def __matmul__(self, other):
        self._check_types(other)
        if self._col_cnt != other._row_cnt:
            raise Exception("Operation is impossible -- row count and column count are different:"
                            + str(self._row_cnt) + " versus " + str(other._col_cnt))

        key_pair = (self.__hash__(), other.__hash__())
        # checking if the cache_map has already that key pair
        if key_pair not in self._cache_map:
            res_matrix = [[0] * other._col_cnt for _ in range(self._row_cnt)]
            for i in range(self._row_cnt):
                for j in range(other._col_cnt):
                        sum = 0
                        for k in range(self._col_cnt):
                            sum += self._matrix[i][k] * other._matrix[k][j]
                        res_matrix[i][j] = sum
            self._cache_map[key_pair] = MatrixUser(res_matrix)
        return self._cache_map[key_pair]
