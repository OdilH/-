import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
x = np.array([13, 20, 17, 15, 16, 12, 16, 14, 10, 11])
y = np.array([1000, 600, 500, 1200, 1000, 1500, 500, 1200, 1700, 2000])

# Вычисляем средние значения
mean_x = np.mean(x)
mean_y = np.mean(y)

# Вычисляем коэффициенты b0 и b1
numerator = sum((x - mean_x) * (y - mean_y))
denominator = sum((x - mean_x) ** 2)
b1 = numerator / denominator
b0 = mean_y - b1 * mean_x

# Находим предсказанные значения y
y_pred = b0 + b1 * x

# Вычисляем сумму квадратов ошибок и стандартную ошибку оценивания
sq_errors = sum((y - y_pred) ** 2)
mse = sq_errors / (len(x) - 2)
rmse = np.sqrt(mse)

# Вычисляем коэффициент корреляции
# correlation_coeff = np.corrcoef(x, y)[0, 1]

# Вычисляем коэффициент корреляции без np.corrcoef
numerator_correlation = np.sum((x - mean_x) * (y - mean_y))
denominator_correlation = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
correlation_coeff = numerator_correlation / denominator_correlation




print("b0 =", b0)
print("b1 =", b1)
print("Уравнение регрессии: y = {:.2f} + {:.2f}x".format(b0, b1))
print("Стандартная ошибка оценивания (RMSE):", rmse)
print("Коэффициент корреляции:", correlation_coeff)

# Визуализация данных и линии регрессии
plt.axis([0, 25, 0, 2500])
plt.scatter(x, y, label='Исходные данные', color='blue')
plt.plot(x, y_pred, label='Линия регрессии', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Линейная регрессия')
plt.show()