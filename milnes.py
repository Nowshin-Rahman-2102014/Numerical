import numpy as np
import matplotlib.pyplot as plt
import math

# Milne's Method for one point (Predictor + Corrector)

# Step 1: Take user input
func_input = input("Enter function f(x, y): ")  # e.g. x + y

def f(x, y):
    return eval(func_input)

x0 = float(input("Enter x0: "))
y0 = float(input("Enter y0: "))
h = float(input("Enter step size h: "))

# Previous y-values
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))
y3 = float(input("Enter y3: "))

# Step 2: Compute f-values
f0 = f(x0, y0)
f1 = f(x0 + h, y1)
f2 = f(x0 + 2*h, y2)
f3 = f(x0 + 3*h, y3)

# Step 3: Predictor formula
y4_pred = y0 + (4*h/3) * (2*f1 - f2 + 2*f3)
print(f"\nPredicted y4 = {y4_pred:.6f}")

# Step 4: Corrector formula
f4_pred = f(x0 + 4*h, y4_pred)
y4_corr = y2 + (h/3) * (f2 + 4*f3 + f4_pred)
print(f"Corrected y4 = {y4_corr:.6f}")

# ---------------- PLOTTING ----------------
# Create x and y values
x = [x0, x0 + h, x0 + 2*h, x0 + 3*h, x0 + 4*h]
y = [y0, y1, y2, y3, y4_corr]  # Using corrected value

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o-b', label="Milne's Corrected Values")
plt.plot(x[:-1] + [x[-1]], [y0, y1, y2, y3, y4_pred], 'o--r', label="Predicted Path")

plt.title("Milne's Predictor-Corrector Method")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
