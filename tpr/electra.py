mas = [[0] * 10 for _ in range(10)]


def compare(cr, f, s, x, y):
    codef = [0] * 6
    codes = [0] * 6
    P = [0] * 6
    N = [0] * 6
    p = 0
    n = 0

    for i in range(6):
        if f[i] < cr[i]['scale'][0]:
            codef[i] = cr[i]['code'][0]
        elif f[i] > cr[i]['scale'][1]:
            codef[i] = cr[i]['code'][2]
        else:
            codef[i] = cr[i]['code'][1]

        if s[i] < cr[i]['scale'][0]:
            codes[i] = cr[i]['code'][0]
        elif s[i] > cr[i]['scale'][1]:
            codes[i] = cr[i]['code'][2]
        else:
            codes[i] = cr[i]['code'][1]

        if codef[i] > codes[i]:
            P[i] = cr[i]['weight']
            N[i] = 0
        if codef[i] < codes[i]:
            P[i] = 0
            N[i] = cr[i]['weight']

    print(f"P{x + 1}{y + 1} = ", end="")
    for i in range(6):
        print(P[i], end="")
        p += P[i]
        if i != 5:
            print(" + ", end="")
    print(f" = {p}")

    print(f"N{x + 1}{y + 1} = ", end="")
    for i in range(6):
        print(N[i], end="")
        n += N[i]
        if i != 5:
            print(" + ", end="")
    print(f" = {n}")

    print(f"D{x + 1}{y + 1} = P{x + 1}{y + 1}/N{x + 1}{y + 1} = {p}/{n}", end="")

    if p == 0:
        if n != 0:
            print(" = infinity > 1, accept")
            return "B"
        else:
            print(" < 1, reject")
    elif n == 0:
        print(" undefined, reject")
    elif p / n > 1:
        print(" > 1, accept")
        ret = round(p / n * 10) / 10
        return str(ret)
    else:
        print(" <= 1, reject")

    print()
    return "-"


def build():
    for i in range(10):
        isend = all(mas[i][j] <= 0 for j in range(10))
        if isend:
            for j in range(10):
                if mas[j][i] != 0:
                    mas[j][i] += 1


def recurse(x):
    for i in range(10):
        isconnected = any(mas[i][j] == x for j in range(10))
        if isconnected:
            for j in range(10):
                if mas[j][i] != 0:
                    mas[j][i] = x + 1


def print_levels(x):
    max_val = max(mas[i][j] for i in range(10) for j in range(10))

    if max_val == 0:
        return 0

    print(f"\n\nLevel number {x}: ", end="")

    for i in range(10):
        for j in range(10):
            if mas[i][j] == max_val:
                print(i + 1, end=" ")
                for z in range(10):
                    mas[i][z] = 0

    return print_levels(x + 1)


def main():
    data = [
        [-300, 3, 5, 180, -10, 1],
        [-120, 5, 6, 200, 0, 3],
        [-100, 1, 9, 1000, -60, 3],
        [-50, 3, 4, 100, -30, 10],
        [-150, 5, 2, 500, -20, 1],
        [-200, 4, 5, 700, -10, 5],
        [-180, 10, 4, 300, 0, 3],
        [-500, 2, 4, 2500, -60, 1],
        [-300, 1, 8, 200, -120, 1],
        [-450, 7, 2, 600, -45, 4]
    ]

    names = [
        "Subscription price",
        "People for joint viewing",
        "Rating",
        "Number of positions",
        "Download delay",
        "Devices per account"
    ]

    weights = [5, 2, 5, 4, 2, 3]

    ispos = [False, True, True, True, False, True]

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
        for i in range(6)
    ]

    for i in range(6):
        print(
            f"Criterion: {cr[i]['name']}, weight: {cr[i]['weight']}, trend upwards: {cr[i]['ispos']}, scale: 1) <{cr[i]['scale'][0]}, 2) from {cr[i]['scale'][0]} to {cr[i]['scale'][1]} 3) >{cr[i]['scale'][1]}")
        print()

    for i in range(10):
        print(f"\n{i + 1} ", end="")
        for j in range(6):
            code = 1 if data[i][j] < cr[j]['scale'][0] else 3 if data[i][j] > cr[j]['scale'][1] else 2
            print(code, end=" ")


if __name__ == "__main__":
    main()
