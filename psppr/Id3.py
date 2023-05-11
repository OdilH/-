
import math
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import graphviz
class DecisionTree:
    def __init__(self):
        self.tree = {}

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def predict(self, X):
        return [self.traverse(self.tree, xi) for xi in X]

    def entropy(self, y):
        _, counts = zip(*Counter(y).items())
        p = [count / len(y) for count in counts]
        return sum(-pi * math.log(pi, 2) for pi in p)

    def split_data(self, X, y, feature, value):
        X1, y1, X2, y2 = [], [], [], []
        for xi, yi in zip(X, y):
            if xi[feature] == value:
                X1.append(xi[:feature] + xi[feature + 1:])
                y1.append(yi)
            else:
                X2.append(xi[:feature] + xi[feature + 1:])
                y2.append(yi)
        return X1, y1, X2, y2

    def information_gain(self, X, y, feature):
        entropy_before = self.entropy(y)
        values = set(xi[feature] for xi in X)
        entropy_after = 0
        for value in values:
            X1, y1, X2, y2 = self.split_data(X, y, feature, value)
            p = len(y1) / len(y)
            entropy_after += p * self.entropy(y1) + (1 - p) * self.entropy(y2)
        return entropy_before - entropy_after

    def choose_feature(self, X, y):
        best_feature = None
        best_information_gain = -1
        for feature in range(len(X[0])):
            ig = self.information_gain(X, y, feature)
            if ig > best_information_gain:
                best_information_gain = ig
                best_feature = feature
        return best_feature

    def build_tree(self, X, y):
        if not y:
            return None
        if len(set(y)) == 1:
            return y[0]
        if not X:
            return Counter(y).most_common(1)[0][0]
        best_feature = self.choose_feature(X, y)
        tree = {best_feature: {}}
        for value in set(xi[best_feature] for xi in X):
            X1, y1, _, _ = self.split_data(X, y, best_feature, value)
            subtree = self.build_tree(X1, y1)
            tree[best_feature][value] = subtree
        return tree

    def traverse(self, tree, x):
        if isinstance(tree, dict):
            feature = next(iter(tree))
            value = x[feature]
            subtree = tree[feature].get(value)
            if subtree is None:
                values = list(tree[feature].keys())
                subtree = tree[feature][values[0]]
            return self.traverse(subtree, x)
        else:
            return tree

def print_tree(tree, indent=''):
    if isinstance(tree, dict):
        feature = list(tree.keys())[0]
        print(indent + feature)
        for value, subtree in tree[feature].items():
            print(indent + '  ' + str(value))
            print_tree(subtree, indent + '    ')
    else:
        print(indent + tree)

# загрузка набора данных
iris = load_iris()
X, y = iris.data, iris.target

# разбиение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# обучение дерева решений
clf = DecisionTree()
clf.fit(X, y)

# вывод структуры дерева решений
print_tree(clf.tree)

# обучение дерева решений
clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(X_train, y_train)

# отображение дерева решений на графике
dot_data = export_graphviz(clf, out_file=None, feature_names=iris.feature_names,
                           class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris_decision_tree")  # сохранение дерева решений в файл
graph.view()  # отображение дерева решений на графике
