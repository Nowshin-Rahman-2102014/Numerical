import numpy as np
import matplotlib.pyplot as plt

# Take function input from user
func_input = input("Enter f(x, y): ")   # Example: x + y

# Convert string input to Python function
def f(x, y):
    return eval(func_input)

# Take initial conditions
x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y0: "))
xn = float(input("Enter final x (xn): "))
h = float(input("Enter step size h: "))

# Euler’s method implementation
x_values = [x0]
y_values = [y0]

x = x0
y = y0

while x < xn:
    y = y + h * f(x, y)   # main formula
    x = x + h
    x_values.append(x)
    y_values.append(y)

# Display final result
print("\nApproximate solution at x =", xn, "is y =", y)

# Print tabular results
print("\nTable of values:")
print("x\t\ty")
for i in range(len(x_values)):
    print(f"{x_values[i]:.4f}\t{y_values[i]:.6f}")

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, 'o-b', label="Euler Approximation")
plt.title("Euler's Method")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
