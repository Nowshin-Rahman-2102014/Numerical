import numpy as np

# Get the size of the system
n = int(input("Enter number of equations: "))

# Input the coefficient matrix
print("Enter the elements of matrix A (each row separated by space):")
A = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)
A = np.array(A)

# Input the constant matrix B
print("Enter the constants (B vector):")
B = np.array(list(map(float, input().split())))

# Check if determinant of A is zero
det_A = np.linalg.det(A)
if det_A == 0:
    print("Determinant is zero! The system has no unique solution.")
else:
    print(f"\nDet(A) = {det_A:.4f}")
    X = []

    for i in range(n):
        # Create a copy of A and replace the i-th column with B
        Ai = np.copy(A)
        Ai[:, i] = B
        det_Ai = np.linalg.det(Ai)
        xi = det_Ai / det_A
        X.append(xi)
        print(f"Det(A{i+1}) = {det_Ai:.4f} -> x{i+1} = {xi:.4f}")

    # Display final solution
    print("\nSolution Vector (X):")
    for i, val in enumerate(X, start=1):
        print(f"x{i} = {val:.6f}")
