import numpy as np
import matplotlib.pyplot as plt

# Входные данные
month = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
price = np.array([13, 20, 17, 15, 16, 12, 16, 14, 10, 11])
sold = np.array([1000, 600, 500, 1200, 1000, 1500, 500, 1200, 1700, 2000])

n = len(month)
sum_price = np.sum(price)
sum_sold = np.sum(sold)
sum_price_squared = np.sum(price ** 2)
sum_price_sold = np.sum(price * sold)

# Находим коэффициенты b0 и b1
A = np.array([[n, sum_price], [sum_price, sum_price_squared]])
B = np.array([sum_sold, sum_price_sold])
b = np.linalg.solve(A, B)

b0, b1 = b

# Предсказанные значения продаж
predicted_sold = b0 + b1 * price

# Расчет стандартной ошибки
errors = predicted_sold - sold
squared_errors = errors ** 2
sum_squared_errors = np.sum(squared_errors)
standard_error = np.sqrt(sum_squared_errors / (n - 2))

# Расчет коэффициента корреляции
mean_price = np.mean(price)
mean_sold = np.mean(sold)
numerator = np.sum((price - mean_price) * (sold - mean_sold))
denominator = np.sqrt(np.sum((price - mean_price) ** 2) * np.sum((sold - mean_sold) ** 2))
correlation_coefficient = numerator / denominator

print("Уравнение линейной регрессии: y = {:.2f} + {:.2f}x".format(b0, b1))
print("Стандартная ошибка: {:.2f}".format(standard_error))
print("Коэффициент корреляции: {:.4f}".format(correlation_coefficient))

# График реальных и предсказанных значений продаж
plt.scatter(price, sold, label='Реальные значения', color='blue')
plt.plot(price, predicted_sold, label='Линия регрессии', color='red')
plt.xlabel('Цена')
plt.ylabel('Продажи')
plt.legend()
plt.show()
