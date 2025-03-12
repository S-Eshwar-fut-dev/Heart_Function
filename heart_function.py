import numpy as np
import matplotlib.pyplot as plt

class Heart_plot:
    def __init__(self, x_range=(-2, 2), y_range=(-2, 2), resolution=400):
        self.x_range = x_range
        self.y_range = y_range
        self.resolution = resolution
        self.x = np.linspace(self.x_range[0], self.x_range[1], self.resolution)
        self.y = np.linspace(self.y_range[0], self.y_range[1], self.resolution)
        self.X, self.Y = np.meshgrid(self.x, self.y)

    def heart_function(self, x, y):
        return (x**2 + y**2 - 1)**3 - (x**2) * (y**3)

    def plot_heart(self):
        Z = self.heart_function(self.X, self.Y)
        plt.figure(figsize=(9, 9))  # Set figure size
        plt.contour(self.X, self.Y, Z, levels=[0], colors='red')  # Plot the contour at level 0

        # Customize the plot
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Plot of (x^2 + y^2 - 1)^3 = x^2 * y^3")
        plt.axhline(0, color='black', linewidth=0.5)  # X-axis
        plt.axvline(0, color='black', linewidth=0.5)  # Y-axis
        plt.grid(True, linestyle='--', linewidth=0.5)

        # Show the plot
        plt.show()

# Create an instance of the class and plot the heart
heart_plot = Heart_plot()
heart_plot.plot_heart()
