import numpy as np
import math

# Picard's Iteration Method
# Equation format: dy/dx = f(x, y)

# Step 1: Take user input
func_input = input("Enter function f(x, y): ")   # e.g. x + y
def f(x, y):
    return eval(func_input)

x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
x = float(input("Enter the value of x where you want to find y: "))
n_iter = int(input("Enter number of iterations: "))
n_points = 100   # For numerical integration (more = more accuracy)

# Step size for integration
h = (x - x0) / n_points
x_vals = np.linspace(x0, x, n_points + 1)

# Step 2: Initialize y-values (start with constant y = y0)
y_vals = np.full_like(x_vals, y0, dtype=float)

# Step 3: Perform Picard iterations
for k in range(n_iter):
    f_vals = f(x_vals, y_vals)
    integral = np.trapezoid(f_vals, x_vals)  # trapezoidal integration
    y_new = y0 + integral
    print(f"Iteration {k+1}: y({x}) = {y_new:.6f}")
    
    # Update y-values for next iteration
    y_vals = y0 + np.array([np.trapezoid(f(x_vals[:i+1], y_vals[:i+1]), x_vals[:i+1]) for i in range(len(x_vals))])

print(f"\nApproximate value of y({x}) after {n_iter} iterations: {y_vals[-1]:.6f}")
