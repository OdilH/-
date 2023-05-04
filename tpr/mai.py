import numpy as np
from math import pow


def first(data, n, index1, index2):
    w = np.ones(10)
    s = np.zeros(10)
    p = np.ones(11)
    p[-1] = 0
    sum = 0

    for i in range(n):
        w[i] = pow(np.prod(data[i]), 1.0 / n)
        sum += w[i]
        print(f"Строка №{i + 1}\nV{index1}{i + 1} = (", end="")
        print("x".join([f"{x:.2f}" for x in data[i]]), end="")
        print(f")^1/{n} = {w[i]:.2f}")

    print(f"\nVi = ", end="")
    print(" + ".join([f"V{i + 1}" for i in range(n)]), end=" =")
    for i in range(n):
        print(f" {w[i]:.2f}", end="")
        if i != n - 1:
            print(" +", end="")
    print(f" = {sum:.2f}\n")

    for i in range(n):
        print(f"Строка №{i + 1}\nW{index2}{i + 1} = {w[i]:.2f}/{sum:.2f} = {w[i] / sum:.2f}")

    print(f"\nW{index2}Y = (", end="")
    print("; ".join([f"{(w[i] / sum):.2f}" for i in range(n)]), end=")\n\n")

    for i in range(n):
        s[i] = np.sum(data[:, i])
        print(
            f"P{i + 1}{index1} = S{i + 1} x W{index2}{i + 1} = {s[i]:.2f} x {w[i] / sum:.2f} = {s[i] * w[i] / sum:.2f}")
        p[i] = s[i] * w[i] / sum

    print(" + ".join([f"P{i + 1}" for i in range(n)]), end=" = ")
    print(" + ".join([f"{p[i]:.2f}" for i in range(n)]), end=" = ")

    p[10] = np.sum(p[:n])
    print(
        f"{p[10]:.2f}\nИС = {(p[10] - n) / (n - 1):.2f}\nОС = ИС/СИ = {(p[10] - n) / (n - 1):.2f}/1.12 = {((p[10] - n) / (n - 1)) / 1.12:.2f}")


def main():
    data1 = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]])

    data2 = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]])
    data3 = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]])

    data4 = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]])

    data5 = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]])

    data6 = np.array([[1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1]])

    print("Таблица с критериями")
    first(data1, 5, "", "2")

    print("\n\nПервый критерий")
    first(data2, 5, "K1", "3K1")

    print("\n\nВторой критерий")
    first(data3, 5, "K2", "3K2")

    print("\n\nТретий критерий")
    first(data4, 5, "K3", "3K3")

    print("\n\nЧетвертый критерий")
    first(data5, 5, "K4", "3K4")

    print("\n\nПятый критерий")
    first(data6, 5, "K5", "3K5")


if __name__ == "__main__":
    main()
