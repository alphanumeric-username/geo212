import numpy as np

def vec(scalar: int | float, dimension: int):
    return scalar * np.ones((dimension,))


def transpose(A: np.ndarray):
    n, m = A.shape
    At = np.zeros((m, n))
    for i in range(n):
        for j in range(m):
            At[j, i] = A[i, j]

    return At


def dot_product(u: np.ndarray, v: np.ndarray):
    if u.shape[0] != v.shape[0]:
        raise ValueError('Matrix shape mismatch: `u` dimension is different from `v`\'s')

    prod = 0
    for i in range(u.shape[0]):
        prod += u[i]*v[i]
    return prod


def matrix_vector_product(A: np.ndarray, v: np.ndarray):
    if v.shape[0] != A.shape[1]:
        raise ValueError('Matrix shape mismatch: `v` dimension is different from `A` number of columns')
    
    n = v.shape[0]
    m = A.shape[0]
    Av = np.empty((m))

    for i in range(m):
        Av[i] = 0
        for j in range(n):
            Av[i] += A[i, j] * v[j]
    
    return Av


def determinant(A: np.ndarray):
    result = 0
    n = A.shape[0]
    
    if n == 1:
        return A[0, 0]
    elif n == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    for i in range(n):
        submatrix = np.zeros((n-1, n-1))
        
        c_skip = 0
        for r in range(0, n-1):
            for c in range(0, n-1):
                if c == i:
                    c_skip = 1
                submatrix[r, c] = A[r+1, c + c_skip]
        
        result += (-1)**i * determinant(submatrix)
    
    return result


def matrix_product(A: np.ndarray, B: np.ndarray):
    """
    Computes the product of 2 bidimensional matrices.

    Parameters
    ----------
    A : np.ndarray
        A n x p matrix.
    B : np.ndarray
        A p x m matrix.

    Returns
    -------
    C : np.ndarray
        The matrix C = AB.
    """
    if len(A.shape) == 1 and len(B.shape) == 1:
        return dot_product(A, B)

    if len(A.shape) == 1:
        aux = A
        A = B
        B = aux
        A = transpose(A)

    if len(B.shape) == 1:
        return matrix_vector_product(A, B)

    if A.shape[1] != B.shape[0]:
        raise ValueError('Matrix shape mismatch: `A` column number is different from `B` row number')

    n = A.shape[0]
    p = A.shape[1]
    m = B.shape[1]
    C = np.empty((n, m))

    for row in range(n):
        for col in range(m):
            C[row, col] = 0
            for i in range(p):
                C[row, col] += A[row, i] * B[i, col]

    return C