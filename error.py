import numpy as np
import math

# Maclaurin expansion of e^x up to n terms
def maclaurin_expansion(x, n):
    return sum([x**k / math.factorial(k) for k in range(n+1)])

# Absolute error
def absolute_error(x_values, n):
    abs_error = 0
    for x in x_values:
        stored_value = np.exp(x)
        computed_value = maclaurin_expansion(x, n)
        abs_error += (stored_value - computed_value) ** 2
    return np.sqrt(abs_error)

# Relative error
def relative_error(x_values, n):
    abs_error = absolute_error(x_values, n)
    stored_sum = sum([np.exp(x)**2 for x in x_values])
    return abs_error / np.sqrt(stored_sum)

# Values of x and n
x_values = [2, 4, 6, 9, 10, 12, 15, 18, 20, 25]
n_values = [10, 20, 50, 75, 100, 125]

# Tabulate results
print("Comparison of stored and computed values of e^x:")
print("n\t Absolute Error\t Relative Error")
for n in n_values:
    abs_error = absolute_error(x_values, n)
    rel_error = relative_error(x_values, n)
    print(f"{n}\t {abs_error:.15e}\t {rel_error:.15e}")

