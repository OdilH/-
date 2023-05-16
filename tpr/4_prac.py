import numpy as np
import matplotlib.pyplot as plt

# Определение области значений
x1 = np.linspace(0, 30, 400)
x2 = np.linspace(0, 30, 400)
x1, x2 = np.meshgrid(x1, x2)

# Определение функции
f = 3*x1 + 4*x2

# Определение ограничений
c1 = x1 + x2 <= 20
c2 = x1 >= 10
c3 = x2 >= 5
c4 = -x1 + 4*x2 <= 20
c5 = np.logical_and(x1 > 0, x2 > 0)  # x1, x2 > 0

# Объединение ограничений
c = np.logical_and(np.logical_and(np.logical_and(c1, c2), np.logical_and(c3, c4)), c5)

fig, ax = plt.subplots()

# Отрисовка функции
cf = ax.contourf(x1, x2, f, levels=50, alpha=0.5)

# Отрисовка области допустимых значений
ax.imshow(c, extent=(0, 30, 0, 30), origin='lower', cmap='Greys', alpha=0.3)

# Добавление подписей к осям
ax.set_xlabel('x1')
ax.set_ylabel('x2')

# Добавление colorbar
fig.colorbar(cf, ax=ax)

plt.show()
