def get_alternative_table(table):
    alternative_table = [['' for _ in range(10)] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if j >= i:
                alternative_table[i][j] = 'X'

    for i in range(10):
        for j in range(i + 1, 10):
            first_flag = False
            second_flag = False
            for k in range(5):
                if k == 0 or k == 3:
                    if table[i][k] > table[j][k]:
                        first_flag = True
                    elif table[i][k] < table[j][k]:
                        second_flag = True
                else:
                    if table[i][k] < table[j][k]:
                        first_flag = True
                    elif table[i][k] > table[j][k]:
                        second_flag = True

            if first_flag and not second_flag:
                alternative_table[j][i] = str(i + 1)
            elif not first_flag and second_flag:
                alternative_table[j][i] = str(j + 1)
            else:
                alternative_table[j][i] = 'N'

    return alternative_table


def bottom_line(table, value, min_val):
    for i in range(10):
        if table[i][value] >= min_val:
            print(i + 1, end=': ')
            for k in range(5):
                print(table[i][k], end='  ')
            print()


def sub_optimization(table, value, min_val):
    number = -1
    priority = 0
    answer = -1
    for i in range(10):
        if table[i][value] >= min_val:
            if table[i][priority] > number:
                number = table[i][priority]
                answer = i

    for i in range(5):
        print(table[answer][i], end='  ')


def lexicographic(table):
    amount = 10
    answer = 0
    while amount > 1:
        for i in range(5):
            for j in range(9):
                if table[answer][i] < table[j + 1][i] and (i == 0 or i == 3):
                    answer = j + 1
                    amount -= 1
                elif table[answer][i] > table[j + 1][i] and (i != 0 and i != 3):
                    answer = j + 1
                    amount -= 1

    for i in range(5):
        print(table[answer][i], end='  ')


if __name__ == '__main__':
    table = [
        [70000, 4, 4, 3, 2],
        [145000, 5, 7, 10, 3],
        [300000, 3, 3, 10, 1],
        [200000, 5, 12, 9, 2],
        [180000, 5, 4, 4, 6],
        [290000, 5, 6, 8, 3],
        [310000, 2, 2, 11, 2],
        [90000, 7, 14, 3, 3],
        [200000, 6, 10, 9, 4],
        [100000, 7, 5, 8, 1]
    ]

    # Построение таблицы альтернатив

    alternative_table = get_alternative_table(table)
    for i in range(10):
        for j in range(10):
            print(alternative_table[i][j], end=' ')
        print()
    # Оптимизация установлением нижней границы
    print('==============================')
    bottom_line(table, 0, 300000)

    # Субоптимизация
    print('==============================')
    sub_optimization(table, 3, 10)

    # Лексикографическая оптимизация
    print()
    print('==============================')
    lexicographic(table)
