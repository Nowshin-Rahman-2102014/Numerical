import numpy as np

def gauss_elimination(A, B):
    # Convert inputs to float arrays
    A = A.astype(float)
    B = B.astype(float)
    n = len(B)

    # Forward Elimination
    for i in range(n):
        # Partial Pivoting - find the row with the max element in current column
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if A[max_row, i] == 0:
            raise ValueError("Matrix is singular or nearly singular!")

        # Swap rows if needed
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            B[[i, max_row]] = B[[max_row, i]]

        # Eliminate entries below pivot
        for j in range(i+1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            B[j] -= factor * B[i]

    # Back Substitution
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (B[i] - np.dot(A[i, i+1:], X[i+1:])) / A[i, i]

    return X


# Example Usage
A = np.array([
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]
])

B = np.array([8, 0, -6])

solution = gauss_elimination(A, B)
print("Solution:", solution)
