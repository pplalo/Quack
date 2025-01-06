import numpy as np
import matplotlib.pyplot as plt

# Define the analytical function
def analytical_function(x):
    return x**2

# Define the range of x values
x = np.linspace(0, 10, 100)  # Adjust range and number of points as needed

# Calculate the analytical results
analytical_results = analytical_function(x)


def numerical_method(x):
    h = 0.01  # Step size
    return (analytical_function(x + h) - analytical_function(x)) / h

# Calculate the numerical results
numerical_results = numerical_method(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, analytical_results, label="Analytical")
plt.plot(x, numerical_results, label="Numerical")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison of Analytical and Numerical Results")
plt.legend()
plt.grid(True)
plt.show()
