# Histogram

import matplotlib.pyplot as plt

prices = [20,25,30,45,50,55,60,65,70,80,90,100,110]
plt.hist(prices, bins=6, color='purple', edgecolor='black')
plt.title('Distribution of House Prices')
plt.xlabel('Price (lakhs)')
plt.ylabel('Number of Houses')
plt.show()