import copy
from math import sqrt

class Tensor:
    def __init__(self, data):
        self.data = copy.deepcopy(data)
        self.shape = self._infer_shape()

    def _is_number(self, value):
        return type(value) == int or type(value) == float

    def _infer_shape(self):
        if self._is_number(self.data):
            return ()

        if len(self.data) == 0:
            return (0,)

        if isinstance(self.data[0], list):
            return (len(self.data), len(self.data[0]))

        return (len(self.data),)

    @property
    def ndim(self):
        return len(self.shape)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        if self.ndim == 0:
            raise TypeError("Scalar tensor has no length.")
        return self.shape[0]

    def __getitem__(self, index):
        return self.data[index]

    def _elementwise(self, other, operation):
        if self._is_number(other):
            return Tensor(self._apply_scalar(self.data, other, operation))

        if isinstance(other, Tensor):
            if self.shape != other.shape:
                raise ValueError(
                    f"Shape mismatch: {self.shape} and {other.shape}"
                )

            return Tensor(self._apply_pair(self.data, other.data, operation))

        return NotImplemented


    # 재귀문법 활용 - self._is_number이 활성화가 끝까지 될때까지 계속 data 안의 요소들을 반복해서 풀어버린다
    def _apply_scalar(self, data, scalar, operation):
        if self._is_number(data):
            return operation(data, scalar)

        return [
            self._apply_scalar(item, scalar, operation)
            for item in data
        ]
    
    def _apply_pair(self, a, b, operation):
        if self._is_number(a) and self._is_number(b):
            return operation(a, b)

        return [
            self._apply_pair(x, y, operation)
            for x, y in zip(a, b)
        ]

    def _add(self, a, b):
        return a + b

    def _subtract(self, a, b):
        return a - b

    def _multiply(self, a, b):
        return a * b

    def __add__(self, other):
        return self._elementwise(other, self._add)

    def __sub__(self, other):
        return self._elementwise(other, self._subtract)

    def __mul__(self, other):
        return self._elementwise(other, self._multiply)

    def dot(self, other):
        if not isinstance(other, Tensor):
            raise TypeError("dot() expects another Tensor.")

        if self.ndim != 1 or other.ndim != 1:
            raise ValueError("dot() only supports 1D vectors.")

        if self.shape != other.shape:
            raise ValueError(
                f"Shape mismatch for dot product: {self.shape} and {other.shape}"
            )

        return sum(a * b for a, b in zip(self.data, other.data))

    def norm(self):
        if self.ndim != 1:
            raise ValueError("norm() only supports 1D vectors.")

        return sqrt(self.dot(self))

    def transpose(self):
        if self.ndim != 2:
            raise ValueError("transpose() only supports 2D matrices.")

        rows, cols = self.shape

        return Tensor([
            [self.data[i][j] for i in range(rows)]
            for j in range(cols)
        ])

    @property
    def T(self):
        return self.transpose()

    def matvec(self, vector):
        if not isinstance(vector, Tensor):
            raise TypeError("matvec() expects a Tensor.")

        if self.ndim != 2 or vector.ndim != 1:
            raise ValueError("matvec() requires a 2D matrix and a 1D vector.")

        rows, cols = self.shape

        if vector.shape[0] != cols:
            raise ValueError(
                f"Shape mismatch: matrix {self.shape} cannot multiply vector {vector.shape}"
            )

        result = []

        for i in range(rows):
            total = 0
            for j in range(cols):
                total += self.data[i][j] * vector.data[j]
            result.append(total)

        return Tensor(result)

    def matmul(self, other):
        if not isinstance(other, Tensor):
            raise TypeError("matmul() expects another Tensor.")

        # vector @ vector -> scalar
        if self.ndim == 1 and other.ndim == 1:
            return self.dot(other)

        # matrix @ vector -> vector
        if self.ndim == 2 and other.ndim == 1:
            return self.matvec(other)

        # vector @ matrix -> vector
        if self.ndim == 1 and other.ndim == 2:
            return self._vector_matrix_mul(other)

        # matrix @ matrix -> matrix
        if self.ndim == 2 and other.ndim == 2:
            return self._matrix_matrix_mul(other)

        raise ValueError("matmul() supports only 1D and 2D tensors.")

    def _vector_matrix_mul(self, matrix):
        vector_length = self.shape[0]
        rows, cols = matrix.shape

        if vector_length != rows:
            raise ValueError(
                f"Shape mismatch: vector {self.shape} cannot multiply matrix {matrix.shape}"
            )

        result = []

        for j in range(cols):
            total = 0
            for i in range(rows):
                total += self.data[i] * matrix.data[i][j]
            result.append(total)

        return Tensor(result)

    def _matrix_matrix_mul(self, other):
        rows_a, cols_a = self.shape
        rows_b, cols_b = other.shape

        if cols_a != rows_b:
            raise ValueError(
                f"Shape mismatch: matrix {self.shape} cannot multiply matrix {other.shape}"
            )

        result = []

        for i in range(rows_a):
            row = []
            for j in range(cols_b):
                total = 0
                for k in range(cols_a):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)

        return Tensor(result)

    def __matmul__(self, other):
        return self.matmul(other)
