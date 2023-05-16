mas = [[0] * 5 for _ in range(10)]
mas2 = []


def compare(data):
    for inf_comp in range(len(data)):
        for criter in range(5):
            if criter == 0:
                if abs(data[inf_comp][criter]) <= 2500:

                    mas[inf_comp][criter] = 15
                elif abs(data[inf_comp][criter]) <= 5000:
                    mas[inf_comp][criter] = 10
                else:
                    mas[inf_comp][criter] = 5

            if criter == 1:
                if abs(data[inf_comp][criter]) <= 10:

                    mas[inf_comp][criter] = 15
                elif abs(data[inf_comp][criter]) <= 20:
                    mas[inf_comp][criter] = 10
                else:
                    mas[inf_comp][criter] = 5

            if criter == 2:
                if abs(data[inf_comp][criter]) >= 14:

                    mas[inf_comp][criter] = 9
                elif abs(data[inf_comp][criter]) >= 7:
                    mas[inf_comp][criter] = 6
                else:
                    mas[inf_comp][criter] = 3

            if criter == 3:
                if abs(data[inf_comp][criter]) >= 22:

                    mas[inf_comp][criter] = 12
                elif abs(data[inf_comp][criter]) >= 19:
                    mas[inf_comp][criter] = 8
                else:
                    mas[inf_comp][criter] = 4

            if criter == 4:
                if abs(data[inf_comp][criter]) >= 12:

                    mas[inf_comp][criter] = 12
                elif abs(data[inf_comp][criter]) >= 8:
                    mas[inf_comp][criter] = 8
                else:
                    mas[inf_comp][criter] = 4



    # Определение альтернатив и критериев
    alternatives = [
        [2500, 15, 20, 24, 7],
        [5000, 10, 10, 22, 8],
        [3500, 20, 8, 20, 6],
        [6000, 5, 7, 18, 7],
        [4500, 5, 9, 24, 9],
        [3000, 25, 6, 16, 5],
        [5500, 10, 8, 19, 7],
        [2500, 5, 7, 17, 8],
        [4000, 20, 7, 22, 6],
        [5500, 15, 10, 19, 9]
    ]

    weights = [5, 5, 3, 4, 4]  # Веса критериев
    tendency = [-1, -1, 1, 1, 1]  # Стремление: -1 для "чем меньше, тем лучше", 1 для "чем больше, тем лучше"

    for i in range(len(alternatives)):
        for j in range(0, len(alternatives)):
            P = 0
            N = 0
            if j != i:
                for k in range(len(weights)):

                    if tendency[k] * alternatives[i][k] > tendency[k] * alternatives[j][k]:
                        P += weights[k]
                    else:

                        N += weights[k]
                m = 0.0
                if N != 0:
                    m = P / N
                    if m > 3:
                        mas2.append(f"D({i + 1},{j + 1}) = {m}")
                #print(f"D({i + 1},{j + 1}) = {m}")

    for i in mas2:
        print(i)


def main():
    data = [
        [-2500, -15, 20, 24, 7],
        [-5000, -10, 10, 22, 8],
        [-3500, -20, 8, 20, 6],
        [-6000, -5, 7, 18, 7],
        [-4500, -5, 9, 24, 9],
        [-3000, -25, 6, 16, 5],
        [-5500, -10, 8, 19, 7],
        [-2500, -5, 7, 17, 8],
        [-4000, -20, 7, 22, 6],
        [-5500, -15, 10, 19, 9]
    ]

    names = [
        "Цена подписки",
        "Время в пути",
        "Кол-во обору",
        "Доступность",
        "Рейтинг"
    ]

    weights = [5, 5, 3, 4, 4]

    ispos = [False, False, True, True, True]

    scale = [
        [-299, -100],
        [2, 4],
        [5, 7],
        [150, 499],
        [-59, -30],
        [2, 4]
    ]

    cr = [
        {
            'name': names[i],
            'weight': weights[i],
            'ispos': ispos[i],
            'scale': scale[i],
            'code': [1, 2, 3]
        }
        for i in range(5)
    ]
    compare(data)


if __name__ == "__main__":
    main()

#
# def compare(cr, f, s, x, y):
#     codef = [0] * 6
#     codes = [0] * 6
#     P = [0] * 6
#     N = [0] * 6
#     p = 0
#     n = 0
#
#     for i in range(6):
#         if f[i] < cr[i]['scale'][0]:
#             codef[i] = cr[i]['code'][0]
#         elif f[i] > cr[i]['scale'][1]:
#             codef[i] = cr[i]['code'][2]
#         else:
#             codef[i] = cr[i]['code'][1]
#
#         if s[i] < cr[i]['scale'][0]:
#             codes[i] = cr[i]['code'][0]
#         elif s[i] > cr[i]['scale'][1]:
#             codes[i] = cr[i]['code'][2]
#         else:
#             codes[i] = cr[i]['code'][1]
#
#         if codef[i] > codes[i]:
#             P[i] = cr[i]['weight']
#             N[i] = 0
#         if codef[i] < codes[i]:
#             P[i] = 0
#             N[i] = cr[i]['weight']
#
#     print(f"P{x + 1}{y + 1} = ", end="")
#     for i in range(6):
#         print(P[i], end="")
#         p += P[i]
#         if i != 5:
#             print(" + ", end="")
#     print(f" = {p}")
#
#     print(f"N{x + 1}{y + 1} = ", end="")
#     for i in range(6):
#         print(N[i], end="")
#         n += N[i]
#         if i != 5:
#             print(" + ", end="")
#     print(f" = {n}")
#
#     print(f"D{x + 1}{y + 1} = P{x + 1}{y + 1}/N{x + 1}{y + 1} = {p}/{n}", end="")
#
#     if p == 0:
#         if n != 0:
#             print(" = infinity > 1, accept")
#             return "B"
#         else:
#             print(" < 1, reject")
#     elif n == 0:
#         print(" undefined, reject")
#     elif p / n > 1:
#         print(" > 1, accept")
#         ret = round(p / n * 10) / 10
#         return str(ret)
#     else:
#         print(" <= 1, reject")
#
#     print()
#     return "-"
#
#
# def build():
#     for i in range(10):
#         isend = all(mas[i][j] <= 0 for j in range(10))
#         if isend:
#             for j in range(10):
#                 if mas[j][i] != 0:
#                     mas[j][i] += 1
#
#
# def recurse(x):
#     for i in range(10):
#         isconnected = any(mas[i][j] == x for j in range(10))
#         if isconnected:
#             for j in range(10):
#                 if mas[j][i] != 0:
#                     mas[j][i] = x + 1
#
#
# def print_levels(x):
#     max_val = max(mas[i][j] for i in range(10) for j in range(10))
#
#     if max_val == 0:
#         return 0
#
#     print(f"\n\nLevel number {x}: ", end="")
#
#     for i in range(10):
#         for j in range(10):
#             if mas[i][j] == max_val:
#                 print(i + 1, end=" ")
#                 for z in range(10):
#                     mas[i][z] = 0
#
#     return print_levels(x + 1)
