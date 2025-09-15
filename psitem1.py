import numpy as np

def average(x):
   return sum(x) / len(x)

# Calculates the variance of a list of numbers using the formula
# σ₁² = (N - 1)⁻¹∑(xᵢ - x̄)²
def var1(x):
   n = len(x)
   mean = average(x)
   return np.sum([(i - mean)**2 for i in x]) / (n - 1)

# Calculates the variance of a list of numbers using the formula
# σ₂² = (N - 1)⁻¹[(∑xᵢ²) - N x̄²]
def var2(x):
   n = len(x)
   mean = average(x)
   return (np.sum([i**2 for i in x]) - n * mean**2) / (n - 1)

# (b) Create N = 100 data points with x_i = 10^9 + u_i where ui are uniformly distributed over [−1, 1].
uData = np.random.uniform(-1, 1, 100) # Stores 100 random numbers between -1 and 1
x = 10**7 + uData # x stores 100 data points, each added with 10^9

# (c) Compute the variance of the data points using var1 and var2.
var1Result = var1(x)
var2Result = var2(x)

# Print the results
print("Variance 1:", var1Result)
print("Variance 2:", var2Result)


# Which is more accurate? Is this always true for any data? Explain why.
if abs(var1Result - var2Result) < np.finfo(float).eps:
   print("The difference is negligible. The two variance calculations are equal.")
elif  abs(var1Result) > abs(var2Result):
   print("var2 is more accurate than var1.")
else:
   print("var1 is more accurate than var2.")
   
print("Further explanations are in the documentation.")


