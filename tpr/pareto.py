import numpy as np


def first(arr):
    n = arr.shape[0]
    ans = np.full((n, n), 'н', dtype='<U1')

    for i in range(n):
        for j in range(i, n):
            ans[i][j] = 'x'

    flag1 = False
    flag2 = False

    for i in range(1, n):
        for j in range(i):
            for z in range(5):
                if arr[i][z] > arr[j][z]:
                    flag1 = True
                if arr[i][z] < arr[j][z]:
                    flag2 = True

            if flag1 and not flag2:
                ans[i][j] = str(i + 1)
            if not flag1 and flag2:
                ans[i][j] = str(j + 1)

            flag1 = False
            flag2 = False

    print("A", end='')
    for i in range(n):
        print(f"{i + 1:3}", end='')
    print()

    for i in range(n):
        for j in range(n):
            if j == 0:
                print(f"{i + 1}", end=' ')
            print(f"{ans[i][j]:3}", end='')
        print()


def second(arr, min, minpos):
    for i in range(10):
        if arr[i][minpos - 1] >= min:
            print(f"{i + 1}: ", end='')
            for j in range(5):
                print(arr[i][j], end=' ')
            print()


def third(arr):
    min = 1000
    minid = -1

    for i in range(10):
        if arr[i][2] >= 4 and abs(arr[i][4]) <= 60:
            if abs(arr[i][0]) < min:
                min = abs(arr[i][0])
                minid = i
            print(f"{i + 1}: ", end='')
            for j in range(5):
                print(arr[i][j], end=' ')
            print()

    print(f"Наилучший {minid + 1}: ", end='')
    for j in range(5):
        print(arr[minid][j], end=' ')


def fourth(arr, ord):
    n = 10
    active = [True] * 10

    for i in range(5):
        max_val = max([arr[j][ord[i] - 1] for j in range(10) if active[j]])
        for j in range(10):
            if arr[j][ord[i] - 1] != max_val and active[j]:
                active[j] = False
                n -= 1
        if n == 1:
            for j in range(10):
                if active[j]:
                    print(f"{j + 1}: ", end='')
                    for z in range(5):
                        print(arr[j][z], end=' ')
                    print()
                    return


data = np.array([
    [-2500, -15, 20, 24, 7],
    [-5000, -10, 10, 22, 8],
    [-3500, -20, 8, 20, 6],
    [-6000, -5, 7, 18, 7],
    [-4500, -5, 9, 24, 9],
    [-3000, -25, 6, 16, 5],
    [-5500, -10, 8, 19, 7],
    [-2500, -5, 7, 17, 8],
    [-4000, -20, 7, 22, 6],
    [-5500, -15, 10, 19, 9], ])

ord_list = [5, 2, 1, 3, 4, 6]

print("Таблица альтернатив:")
first(data)
print()
print("------------------------------------------------------------------------------------------------")
print()
print("\nУстановка верхней границы 8 по критерию 3:")
second(data, 8, 3)
print()
print("------------------------------------------------------------------------------------------------")
print()
print("\nСубоптимизация по критерию 1 с установкой границы 5 по критерию 3 и 60 по критерию 5:")
third(data)
print()
print()
print("------------------------------------------------------------------------------------------------")
print("\n\nЛексикографическая оптимизация по критериям 5, 2, 1, 3, 4:")
fourth(data, ord_list)

