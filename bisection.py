import math

# Take user input for the function
func_input = input("Enter function f(x): ")   # e.g. x**3 - x - 2

# Convert input string into a Python function
def f(x):
    return eval(func_input)

# Take interval and tolerance input
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tol = float(input("Enter tolerance (e.g. 0.0001): "))

# Check if root exists in the interval
if f(a) * f(b) > 0:
    print("No root found in this interval! f(a) and f(b) must have opposite signs.")
else:
    print("\nIteration\t a\t\t b\t\t c\t\t f(c)")
    iteration = 1
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)
        print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {fc:.6f}")

        if fc == 0:
            break
        elif f(a) * fc < 0:
            b = c
        else:
            a = c

        iteration += 1

    print(f"\nApproximate Root: {(a + b) / 2:.6f}")
