from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [12, 54, 34, 67, 84, 23, 46, 52, 87, 79]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

x2 = sorted(x)
y2 = y

plt.plot(x, y, 'g', label='line one', linewidth=5)
plt.plot(x2, y2, 'c', label='line two', linewidth=5)

plt.title('info_blg')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.grid(True, color='w')

plt.show()