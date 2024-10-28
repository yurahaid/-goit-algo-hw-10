import random

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 3

def is_inside(x, y):
    return y <= f(x)

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

x_max = 2
y_max = f(x_max)


for points_count in [150, 15000, 150000]:
    # Генерація випадкових точок
    points = [(random.uniform(0, x_max), random.uniform(0, y_max)) for _ in range(points_count)]

    # Відбір точок, що знаходяться всередині фігури
    inside_points = [point for point in points if is_inside(point[0], point[1])]

    # Кількість усіх точок та точок всередині
    N = len(points)
    M = len(inside_points)

    # Обчислення інтеграла (Теоретична площа)
    S, _ = spi.quad(f, a, b)

    Sm = (M / N) * (x_max * y_max)  # Площа за методом Монте-Карло

    # Виведення результатів
    print(f"Кількість точок всередині фігури: {M}, загальна кількість точок: {N}")
    print(f"Теоретична площа: {S}, площа за методом Монте-Карло: {Sm}")