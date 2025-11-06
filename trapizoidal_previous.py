import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad  # for actual true value

# Define the function
def f(t):
    return 200 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t

# Limits
a = 8
b = 30

# Single segment trapezoidal rule
I_trap = (b - a) / 2 * (f(a) + f(b))

# Find true value using numerical integration (very accurate)
true_value, _ = quad(f, a, b)

# Error calculations
true_error = true_value - I_trap
abs_relative_error = abs(true_error / true_value) * 100

# Display results
print(f"Trapezoidal Approximation (single segment): {I_trap:.6f}")
print(f"True Value (using quad): {true_value:.6f}")
print(f"True Error (E_t): {true_error:.6f}")
print(f"Absolute Relative True Error: {abs_relative_error:.4f}%")

# Plotting
t_vals = np.linspace(a, b, 100)
f_vals = [f(t) for t in t_vals]

plt.plot(t_vals, f_vals, 'b-', label='f(t)')
plt.fill_between(t_vals, f_vals, color='lightblue', alpha=0.4)
plt.scatter([a, b], [f(a), f(b)], color='red')
plt.title('Vertical Distance Function (Trapezoidal Approximation)')
plt.xlabel('t (seconds)')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.show()

# Tabular data
print("\nTabular Data:")
print("t\tf(t)")
for t in np.linspace(a, b, 5):
    print(f"{t:.2f}\t{f(t):.6f}")
