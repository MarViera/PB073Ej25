import matplotlib.pyplot as plt
import random

x_numbers = range(1,11)
y_numbers = []
for i in range(10):
    y_numbers.append(random.randint(1,10))

plt.plot(x_numbers, y_numbers, 'o')
plt.show()
