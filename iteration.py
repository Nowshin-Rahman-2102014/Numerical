import math

# User inputs the function in the form g(x)
func_input = input("Enter g(x) for iteration (x = g(x)): ")  # e.g., math.cos(x)
def g(x):
    return eval(func_input)

# Initial guess
x0 = float(input("Enter initial guess x0: "))

# Tolerance and max iterations
tol = float(input("Enter tolerance (e.g., 0.0001): "))
max_iter = int(input("Enter maximum number of iterations: "))

print("\nIteration\t x_n\t\t x_(n+1)\t |x_(n+1)-x_n|")
for i in range(1, max_iter+1):
    x1 = g(x0)
    error = abs(x1 - x0)
    print(f"{i}\t\t {x0:.6f}\t {x1:.6f}\t {error:.6f}")
    
    if error < tol:
        print(f"\nConverged to {x1:.6f} after {i} iterations.")
        break
    
    x0 = x1
else:
    print("\nDid not converge within the maximum number of iterations.")
