import math
import numpy as np
import matplotlib.pyplot as plt

# Take user input for the function
func_input = input("Enter function f(x): ")   # Example: x**2 + 3*x + 2

# Convert input string into a Python function
def f(x):
    return eval(func_input)

# Take integration limits and number of subintervals
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals (n): "))

# Step size
h = (b - a) / n

# Generate x and y values
x = np.linspace(a, b, n + 1)
y = [f(i) for i in x]

# Apply Trapezoidal Rule
sum_fx = y[0] + y[-1] + 2 * sum(y[1:-1])
result = (h / 2) * sum_fx

print(f"\nApproximate value of integration: {result:.6f}")

# =================== PLOT SECTION ===================

# Smooth curve for function
x_curve = np.linspace(a, b, 300)
y_curve = [f(i) for i in x_curve]

plt.figure(figsize=(8, 6))

# Plot the function curve
plt.plot(x_curve, y_curve, 'b', label='f(x)')

# Fill trapezoidal regions
for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, y[i], y[i+1], 0]
    plt.fill(xs, ys, color='skyblue', alpha=0.4, edgecolor='black', linewidth=1)

# Mark data points
plt.scatter(x, y, color='red', zorder=5, label='Data Points')

# Labels, title, legend
plt.title("Trapezoidal Rule Visualization", fontsize=14)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
