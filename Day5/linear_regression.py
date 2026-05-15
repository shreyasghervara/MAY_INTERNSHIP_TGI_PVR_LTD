# linear_regression.py

import numpy as np
import matplotlib.pyplot as plt

# Study hours vs Marks dataset
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
marks = np.array([40, 50, 55, 65, 70, 80, 85, 92])

# Perform Linear Regression
slope, intercept = np.polyfit(hours, marks, 1)

# Print regression formula
print("Linear Regression Formula:")
print(f"marks = {slope:.2f} * hours + {intercept:.2f}")

# Predict marks for a fixed value
predict_hours = 5
predicted_marks = slope * predict_hours + intercept

print(f"\nPredicted marks for {predict_hours} study hours: {predicted_marks:.2f}")

# Plot actual data points
plt.scatter(hours, marks, color='blue', label='Actual Data')

# Plot regression line
plt.plot(hours, slope * hours + intercept,
         color='red', label='Regression Line')

# Labels and title
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Study Hours vs Marks')

plt.legend()
plt.grid(True)

# Save graph
plt.savefig('regression.png')

print("\nGraph saved as 'regression.png'")