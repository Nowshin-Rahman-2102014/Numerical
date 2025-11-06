import math

# Take user input for f(x)
func_input = input("Enter function f(x): ")   # e.g. x**3 - x - 2
# Take user input for f'(x)
deriv_input = input("Enter derivative f'(x): ")  # e.g. 3*x**2 - 1

# Convert the strings to functions
def f(x):
    return eval(func_input)

def df(x):
    return eval(deriv_input)

# Input initial guess and tolerance
x0 = float(input("Enter initial guess x0: "))
tol = float(input("Enter tolerance (e.g. 0.0001): "))
max_iter = int(input("Enter maximum iterations: "))

print("\nIteration\t x\t\t f(x)")
print("------------------------------------------")

for i in range(max_iter):
    fx = f(x0)
    dfx = df(x0)

    if dfx == 0:
        print("Derivative is zero! No solution found.")
        break

    x1 = x0 - fx / dfx

    print(f"{i+1}\t\t {x0:.6f}\t {fx:.6f}")

    if abs(x1 - x0) < tol:
        print("\nApproximate root:", round(x1, 6))
        break

    x0 = x1
else:
    print("\nDid not converge within given iterations.")
