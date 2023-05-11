import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self):
        self.weights = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, x, y, iterations, lr):
        num_samples, num_features = x.shape
        self.weights = np.random.rand(num_features)
        bias = np.random.rand(1)

        # Gradient descent
        for _ in range(iterations):
            linear_model = np.dot(x, self.weights) + bias
            y_predicted = self.sigmoid(linear_model)

            # Compute gradients
            dw = (1 / num_samples) * np.dot(x.T, (y_predicted - y))
            db = (1 / num_samples) * np.sum(y_predicted - y)

            # Update weights
            self.weights -= lr * dw
            bias -= lr * db

    def predict_probability(self, x):
        linear_model = np.dot(x, self.weights)
        return self.sigmoid(linear_model)

    def predict(self, x, threshold):
        probabilities = self.predict_probability(x)
        return [1 if i > threshold else 0 for i in probabilities]

    def loss(self, y, y_pred):
        return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))


x = np.array([
    [6.225953, 0],
    [7.090864, 0],
    [0.938448, 0],
    [4.883051, 0],
    [4.585243, 0],
    [4.767659, 0],
    [4.263978, 0],
    [7.028656, 0],
    [8.734312, 0],
    [0.455714, 0],
    [6.795691, 0],
    [3.377665, 0],
    [6.057999, 0],
    [5.284733, 0],
    [3.516788, 0],
    [4.869974, 0],
    [9.433221, 0],
    [9.159726, 0],
    [1.890128, 0],
    [1.940041, 0],
    [5.729737, 0],
    [3.523604, 0],
    [4.273961, 0],
    [9.553667, 0],
    [5.684523, 0],
    [0.413468, 0],
    [3.510537, 0],
    [0.252018, 0],
    [6.800133, 0],
    [7.226425, 0],
    [6.168154, 0],
    [4.755167, 0],
    [6.120781, 0],
    [9.241946, 0],
    [2.755540, 0],
    [4.834614, 0],
    [7.755265, 0],
    [8.361042, 0],
    [5.347481, 0],
    [2.938204, 0],
    [9.646393, 0],
    [2.097223, 0],
    [7.023243, 0],
    [4.152719, 0],
    [2.182873, 0],
    [5.029063, 0],
    [1.875534, 0],
    [2.075754, 0],
    [6.338961, 0],
    [5.299832, 0],
    [24.68904, 1],
    [21.00722, 1],
    [19.38777, 1],
    [23.63270, 1],
    [19.64973, 1],
    [19.25936, 1],
    [18.69575, 1],
    [17.41184, 1],
    [16.85810, 1],
    [16.39972, 1],
    [21.96098, 1],
    [24.18971, 1],
    [23.48216, 1],
    [17.78697, 1],
    [23.71791, 1],
    [23.08646, 1],
    [20.26889, 1],
    [19.41455, 1],
    [20.84174, 1],
    [20.93166, 1],
    [23.16128, 1],
    [20.60788, 1],
    [21.31941, 1],
    [24.57976, 1],
    [16.38619, 1],
    [21.54752, 1],
    [22.16996, 1],
    [17.77842, 1],
    [18.71960, 1],
    [23.44474, 1], [19.74865, 1],
    [15.44030, 1],
    [20.62114, 1],
    [18.00286, 1],
    [22.63674, 1],
    [16.24574, 1],
    [22.37409, 1],
    [15.17103, 1],
    [15.54813, 1],
    [18.59273, 1], [15.05515, 1],
    [18.54310, 1],
    [16.51185, 1],
    [23.72693, 1],
    [23.11799, 1],
    [22.87555, 1],
    [18.79101, 1],
    [16.61081, 1],
    [21.42116, 1],
    [24.99244, 1]])

y = np.array(
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
     0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1,
     0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1]
)


log_reg = LogisticRegression()
log_reg.fit(x, y, iterations=1000, lr=0.01)

y_pred = log_reg.predict(x, threshold=0.5)

# Получаем предсказанные вероятности
y_pred_proba = log_reg.predict_probability(x)

plt.figure(figsize=(10,6))

# График реальных классов
plt.scatter(x[y == 0][:, 0], y[y == 0], color='blue', label='Class 0')
plt.scatter(x[y == 1][:, 0], y[y == 1], color='green', label='Class 1')

# График предсказанных вероятностей
plt.scatter(x[:, 0], y_pred_proba, color='red', label='Predicted probabilities')

plt.title('Logistic Regression Predictions')
plt.xlabel('Feature value')
plt.ylabel('Class/Predicted probability')
plt.legend()

plt.show()
