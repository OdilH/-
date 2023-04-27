from prettytable import PrettyTable
import numpy as np
from sympy import diff, sqrt


def func(x1, x2):  # Функция вывода значения функции согласно входным координатам x1 и x2
    return round(eval(F), roundnum)


def getstep(x1, x2):  # Функция вывода шага на основе градиента функции и матрицы Гессе
    # Создаём матрицу Гессе на основе целевой функции
    mgesse = np.array([[eval(str(diff(diff(F, 'x1'), 'x1'))), eval(str(diff(diff(F, 'x1'), 'x2')))],
                       [eval(str(diff(diff(F, 'x2'), 'x1'))), eval(str(diff(diff(F, 'x2'), 'x2')))]])
    # Вычисляем шаг на основе матрицы Гессе и градиента функции
    step = np.array([grad(x1, x2)[0], grad(x1, x2)[1]]).dot(np.array([[grad(x1, x2)[0]], [grad(x1, x2)[1]]]))[0] \
           / np.array([grad(x1, x2)[0], grad(x1, x2)[1]]).dot(mgesse.dot(
            np.array([[grad(x1, x2)[0]], [grad(x1, x2)[1]]])))[0]
    return step


def grad(x1, x2):  # Вычисление градиента функции
    return [eval(str(diff(F, 'x1'))), eval(str(diff(F, 'x2')))]


def newcoords():  # Вывод новых координат на основе исходных, шага и градиента функции
    return [x1p - getstep(x1p, x2p) * grad(x1p, x2p)[0],
            x2p - getstep(x1p, x2p) * grad(x1p, x2p)[1]]


F = '7*x1**2+2*x1*x2+5*x2**2+x1-10*x2'  # Целевая функция
e = 0.0001  # Точность
x1p = 1  # Изначальная координата x1
x2p = 1  # Изначальная координата x2
roundnum = 14  # Округление после запятой для избежания ошибки с плавающей точкой
iteramount = 0  # Счётчик итераций
tab = [[x1p, x2p, func(x1p, x2p)]]  # Ввод в таблицу нулевой точки согласно входным данным
while sqrt(grad(x1p, x2p)[0] ** 2 + grad(x1p, x2p)[1] ** 2) > e:  # Проверим условие завершения поиска
    # Применяем новые координаты
    x1p, x2p = round(float(newcoords()[0]), roundnum), round(float(newcoords()[1]), roundnum)
    tab.append([x1p, x2p, func(x1p, x2p)])  # Добавляем новые координаты и значение функции в таблицу
    iteramount += 1  # Добавляем единицу к счётчику итерций
table = PrettyTable(['Точка', 'X1', 'X2', 'Значение функции'])  # Вводим заголовки столбцов таблицы с выводом
for s in tab:  # Каждый элемент таблицы tab
    table.add_row(['X(' + str(tab.index(s)) + ')', s[0], s[1], s[2]])  # Записываем в таблицу, добавляя номер точки
print('\nЦелевая функция: F(x1, x2)=' + F + '\n')  # Вывод целевой функции
print(table)  # Выводим таблицу
print('\nИтераций произведено: ' + str(iteramount))  # Выводим количество итераций
