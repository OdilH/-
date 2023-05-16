def main():
    matrix = [
        [None, None, "80.0", "125.0", None],
        [None, None, "X1", "X2", "A"],
        ["0.0", "X3", "0.01", "0.02", "160.0"],
        ["0.0", "X4", "0.02", "0.01", "120.0"],
        ["0.0", "X5", "0.04", "0.01", "150.0"],
        [None, None, "-80.0", "-125.0", None]
    ]
    upgrade_matrix(matrix)
# Замена None на пустые строки

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] is None:
                matrix[i][j] = ""


def upgrade_matrix(matrix):
    print("====================MATRIX====================")
    for i in range(6):
        for j in range(5):
            print(f"{matrix[i][j]:<10}", end="")
        print()

    # 2 и 3 столбец чекаем дельту (5 строка)
    min1 = 0
    index1 = 0
    if float(matrix[5][2]) < min1:
        min1 = float(matrix[5][2])
        index1 = 2
    if float(matrix[5][3]) < min1:
        min1 = float(matrix[5][3])
        index1 = 3
    if min1 == 0:
        return

    # 2, 3, 4 строка ищем строку (4 столбец)
    min2 = float(matrix[2][4]) / float(matrix[2][index1])
    index2 = 2
    if float(matrix[3][4]) / float(matrix[3][index1]) < min2:
        min2 = float(matrix[3][4]) / float(matrix[3][index1])
        index2 = 3
    if float(matrix[4][4]) / float(matrix[4][index1]) < min2:
        min2 = float(matrix[4][4]) / float(matrix[4][index1])
        index2 = 4

    temp_matrix = [[None] * 3 for _ in range(4)]

    temp1 = matrix[1][index1]
    matrix[1][index1] = matrix[index2][1]
    matrix[index2][1] = temp1

    temp2 = matrix[0][index1]
    matrix[0][index1] = matrix[index2][0]
    matrix[index2][0] = temp2

    employ = float(matrix[index2][index1])

    temp_matrix[0][index1 - 2] = (float(matrix[2][index1]) / employ * -1)
    temp_matrix[1][index1 - 2] = (float(matrix[3][index1]) / employ * -1)
    temp_matrix[2][index1 - 2] = (float(matrix[4][index1]) / employ * -1)
    temp_matrix[3][index1 - 2] = (float(matrix[5][index1]) / employ * -1)

    temp_matrix[index2 - 2][0] = (float(matrix[index2][2]) / employ)
    temp_matrix[index2 - 2][1] = (float(matrix[index2][3]) / employ)
    temp_matrix[index2 - 2][2] = (float(matrix[index2][4]) / employ)

    for i in range(3):
        for j in range(3):
            if temp_matrix[i][j] is None:
                temp_matrix[i][j] = (
                        (float(matrix[i + 2][j + 2]) * float(matrix[index2][index1])
                         - float(matrix[index2][j + 2]) * float(matrix[i + 2][index1]))
                        / float(matrix[index2][index1])
                )

    if index1 == 3:
        temp_matrix[3][0] = (
                (float(matrix[5][2]) * float(matrix[index2][index1])
                 - float(matrix[index2][2]) * float(matrix[5][index1]))
                / float(matrix[index2][index1])
        )
    else:
        temp_matrix[3][1] = (
                (float(matrix[5][3]) * float(matrix[index2][index1])
                 - float(matrix[index2][3]) * float(matrix[5][index1]))
                / float(matrix[index2][index1])
        )

    temp_matrix[index2 - 2][index1 - 2] = 1 / float(matrix[index2][index1])

    for i in range(3):
        for j in range(3):
            matrix[i + 2][j + 2] = str(round(temp_matrix[i][j], 2))

    matrix[5][2] = str(round(temp_matrix[3][0], 2))
    matrix[5][3] = str(round(temp_matrix[3][1], 2))

    Q = (
            float(matrix[2][0]) * float(matrix[2][4])
            + float(matrix[3][0]) * float(matrix[3][4])
            + float(matrix[4][0]) * float(matrix[4][4])
    )
    matrix[5][4] = str(Q)

    upgrade_matrix(matrix)


if __name__ == "__main__":
    main()

