def lagrange_interpolation(x_points, y_points, value):
    n = len(x_points)
    result = 0

    # Apply Lagrange formula
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (value - x_points[j]) / (x_points[i] - x_points[j])
        result += term

    return result


# === Main Program ===
n = int(input("Enter number of data points: "))

x_points = []
y_points = []

print("Enter the data points (x and y):")
for i in range(n):
    x, y = map(float, input(f"x[{i}], y[{i}]: ").split())
    x_points.append(x)
    y_points.append(y)

value = float(input("Enter the value of x to interpolate: "))

result = lagrange_interpolation(x_points, y_points, value)
print(f"\nEstimated value at x = {value} is {result:.6f}")
