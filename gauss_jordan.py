import numpy as np

def gauss_jordan(A, B):
    # Convert to float arrays for accuracy
    A = A.astype(float)
    B = B.astype(float)
    n = len(B)

    # Forward and Backward Elimination
    for i in range(n):
        # Partial Pivoting (to avoid division by zero)
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if A[max_row, i] == 0:
            raise ValueError("Matrix is singular or nearly singular!")

        # Swap rows in A and B
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            B[[i, max_row]] = B[[max_row, i]]

        # Make pivot = 1 (Normalize the pivot row)
        pivot = A[i, i]
        A[i, :] = A[i, :] / pivot
        B[i] = B[i] / pivot

        # Eliminate all other entries in current column
        for j in range(n):
            if j != i:
                factor = A[j, i]
                A[j, :] -= factor * A[i, :]
                B[j] -= factor * B[i]

    return B  # Now B holds the final solution vector


# Example Usage
A = np.array([
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]
])

B = np.array([8, 0, -6])

solution = gauss_jordan(A, B)
print("Solution:", solution)
