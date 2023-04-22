from fractions import Fraction
import math


print(Fraction(float(1)), float(Fraction('1/5')))

size_mtr = {1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49,
            11: 1.51,
            12: 1.48,
            13: 1.56,
            14: 1.57,
            15: 1.59}


n = int(input('Введите количество критериев: '))
m = int(input('Введите количество альтернатив: '))
cr = list(map(str, input("Введите название критериев через пробел: ").strip().split()))[:n]
alternatives = list(map(str, input("Введите название альтернатив через пробел: ").strip().split()))[:m]


C = [[0] * n for i in range(n)]
W_A = [0] * n
W = [[0] * m for g in range(m)]
V = [1] * (n + 1)
V[n] = 0
Result = [0] * m
S = [0] * n
sum = 0


for i in range(n):
    buf = list(map(str, input(
        'Введите интенсивность относительной важности между K{0} и K{1}-K{2}: '.format(i + 1, i + 1,
                                                                                       n)).strip().split()))[:n - i]
    value = 0
    for y in range(n):
        if C[i][y] == 0:
            if '/' not in buf[value]:
                C[i][y] = Fraction(float(buf[value]))
            else:
                C[i][y] = Fraction(buf[value])
            value += 1

    for y in range(i + 1, n):
        C[y][i] = 1 / C[i][y]

    for g in range(n):
        V[i] *= float(C[i][g])
    V[i] = pow(V[i], 1/n)
    V[n] += V[i]

for i in range(n):
    W_A[i] = float(V[i] / V[n])

for i in range(n):
    for g in range(n):
        S[i] += C[g][i]


for i in range(n):
    sum += float(S[i]) * W_A[i]

if (((sum - n) / (n - 1)) / size_mtr[n]) > 0.10:
    print('Матрица не согласована', ((sum - n) / (n - 1) / size_mtr[n]))
    exit()


for p in range(n):
    print()
    sum = 0
    V = [1] * (m + 1)
    V[m] = 0
    S = [0] * m
    C = [[0] * m for i in range(m)]

    for i in range(0, m):
        buf = list(map(str, input(
            'Введите интенсивность относительной важности между A{0} и A{1}-A{2} для K{3}: '.format(i + 1, i + 1, m,
                                                                                                    p + 1)).strip().split()))[
              :m - i]

        value = 0
        for y in range(m):
            if C[i][y] == 0:
                if '/' not in buf[value]:
                    C[i][y] = Fraction(float(buf[value]))
                else:
                    C[i][y] = Fraction(buf[value])
                value += 1

        for y in range(i, m):
            C[y][i] = 1 / C[i][y]

        for g in range(m):
            V[i] *= float(C[i][g])
        V[i] = pow(V[i], 1 / m)
        V[m] += V[i]

    for i in range(0, m):
        W[p][i] = float(V[i] / V[m])

    for i in range(m):
        for g in range(m):
            S[i] += C[g][i]

    for i in range(m):
        sum += float(S[i]) * W[p][i]

    if ((sum - m) / (m - 1) / size_mtr[m]) > 0.10:
        print('Матрица не согласована', ((sum - m) / (m - 1) / size_mtr[n]))
        exit()

for i in range(0, m):
    for y in range(0, n):
        Result[i] += W_A[y]*W[y][i]

for i in range(m):
    print('Альтернатива: ', alternatives[i], ' - приоритет равен ', round(Result[i], 3))