import matplotlib.pyplot as plt

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8,
            55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)#13
print(years,len(years))
input()
plt.plot(years, nyc_temp, marker='*')
plt.show()
