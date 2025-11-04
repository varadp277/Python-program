# Bar chart 

import matplotlib.pyplot as plt

products = ["Google","Microsoft","OpenAI","Perplexity"]
sales = [150, 130, 200, 90]
plt.bar(products, sales)
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()