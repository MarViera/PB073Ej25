import matplotlib.pyplot as plt
import random

x_numbers = []
y_numbers = []
for i in range(10):
    x_numbers.append(i+1)
    y_numbers.append(random.randint(1,10))


plt.plot(x_numbers, y_numbers)
plt.show()

