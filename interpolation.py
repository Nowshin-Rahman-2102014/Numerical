import numpy as np
import math

# ---------- Forward Difference Table ----------
def forward_difference_table(x, y):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    return diff_table

# ---------- Backward Difference Table ----------
def backward_difference_table(x, y):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]
    return diff_table

# ---------- Newton Forward Interpolation ----------
def newton_forward(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    diff_table = forward_difference_table(x, y)
    p = (value - x[0]) / h

    result = y[0]
    for i in range(1, n):
        term = diff_table[0][i]
        for j in range(i):
            term *= (p - j)
        result += term / math.factorial(i)
    return result

# ---------- Newton Backward Interpolation ----------
def newton_backward(x, y, value):
    n = len(x)
    h = x[1] - x[0]
    diff_table = backward_difference_table(x, y)
    p = (value - x[-1]) / h

    result = y[-1]
    for i in range(1, n):
        term = diff_table[-1][i]
        for j in range(i):
            term *= (p + j)
        result += term / math.factorial(i)
    return result

# ---------- Main Program ----------
n = int(input("Enter number of data points: "))
x = np.zeros(n)
y = np.zeros(n)

print("Enter the data points (x and y):")
for i in range(n):
    x[i], y[i] = map(float, input(f"x[{i}], y[{i}]: ").split())

value = float(input("Enter the value of x to interpolate: "))

# Decide whether to use forward or backward interpolation
midpoint = (x[0] + x[-1]) / 2

if value <= midpoint:
    print("\nUsing Newton's Forward Interpolation...")
    result = newton_forward(x, y, value)
else:
    print("\nUsing Newton's Backward Interpolation...")
    result = newton_backward(x, y, value)

print(f"Estimated value at x = {value} is {result:.6f}")
#Enter number of data points: 4
#Enter the data points (x and y):
#x[0], y[0]: 0 1
#x[1], y[1]: 1 2.718
#x[2], y[2]: 2 7.389
#x[3], y[3]: 3 20.085
#Enter the value of x to interpolate: 1.5
