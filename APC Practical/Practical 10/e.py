# Scatter plot

import matplotlib.pyplot as plt

height = [150, 160, 165, 170, 175, 180, 185, 190]
weight = [50, 60, 62, 68, 72, 78, 85, 90]
plt.scatter(height, weight)
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()