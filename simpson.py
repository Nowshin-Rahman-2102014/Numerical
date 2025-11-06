import math
import numpy as np
import matplotlib.pyplot as plt

# Take user input for the function
func_input = input("Enter function f(x): ")  # e.g. x**3 + 2*x**2 + x + 1

# Convert input string into Python function
def f(x):
    return eval(func_input)

# Take integration limits and number of subintervals
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n: "))

# Step size
h = (b - a) / n

# ---------------- Simpson 1/3 Rule ----------------
def simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 rule requires an even number of subintervals (n).")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]
    result += 4 * sum(y[1:-1:2])  # odd terms
    result += 2 * sum(y[2:-1:2])  # even terms

    result *= h / 3
    return result, x, y

# ---------------- Simpson 3/8 Rule ----------------
def simpson_three_eighth(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Simpson 3/8 rule requires n to be divisible by 3.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = [f(xi) for xi in x]

    result = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 != 0:
            result += 3 * y[i]
        else:
            result += 2 * y[i]

    result *= 3 * h / 8
    return result, x, y

# ---------------- User Choice ----------------
choice = input("Choose method: 1 for Simpson 1/3, 2 for Simpson 3/8: ")

if choice == '1':
    approx, x_vals, y_vals = simpson_one_third(f, a, b, n)
    method_name = "Simpson's 1/3 Rule"
elif choice == '2':
    approx, x_vals, y_vals = simpson_three_eighth(f, a, b, n)
    method_name = "Simpson's 3/8 Rule"
else:
    raise ValueError("Invalid choice!")

print(f"\nApproximate value of integration ({method_name}) = {approx:.6f}")

# ---------------- Plot the Graph ----------------
x_plot = np.linspace(a, b, 200)
y_plot = [f(xi) for xi in x_plot]

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, 'b', label='f(x)')
plt.fill_between(x_plot, y_plot, color='skyblue', alpha=0.4)
plt.scatter(x_vals, y_vals, color='red', zorder=5, label='Subinterval points')

plt.title(f"Integration using {method_name}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
# ---------------- Tabular Data ----------------
print("\nTabular Data:")
print("x\tf(x)")
for xi, yi in zip(x_vals, y_vals):
    print(f"{xi:.6f}\t{yi:.6f}")    
    