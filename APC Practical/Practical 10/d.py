# Pie chart 

import matplotlib.pyplot as plt

labels = ['Rent', 'Food', 'Savings', 'Transport', 'Other']
sizes = [30, 25, 20, 15, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Monthly Income Spending')
plt.axis('equal')
plt.show()