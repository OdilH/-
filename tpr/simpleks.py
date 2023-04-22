# Переменные для работы программы
matrix = []
count = 0
Cj = []
Xj = []

F = list(map(str, input("Введите функцию: ").strip().split()))  # Ввод функции
aspiration = str(input("Какое стремление (min/max): "))  # Ввод стремления

for item in F:  # Заполнение Cj и Xj
    if 'x' in item:
        count += 1
        Xj.append(item)
    if item.isdigit():
        if aspiration == 'min':
            Cj.append(-1 * int(item))
        else:
            Cj.append(int(item))


q = int(input("Введите количество ограничений: "))  # Ввод количества ограничений
for i in range(q):
    Q = list(map(str, input("Введите ограничение: ").strip().split()))
    if Q[-2] != '=':
        matrix.append(Q)

matrix2 = [[0] * q for p in range(count + 1)]
matrix2_basic = [[0] * q for p in range(count + 1)]
Cb = []
Xb = []

for y in range(q):  # Заполнение Cb
    i = 0
    Cb.append(0)
    Xb.append('x{0}'.format(count + y + 1))
    while i <= count:
        for item in matrix[y]:
            if item.isdigit():
                matrix2[i][y] = int(item)
                matrix2_basic[i][y] = int(item)
                i += 1


b = False
Result = []

for i in range(count):  # Расчёт дельты
    r = 0
    for y in range(q):
        r += Cb[y] * matrix2[i][y]
    Result.append(r - Cj[i])
for item in Result:  # Проверка на положительность дельты
    if item < 0:
        b = True

while b:
    b = False

    column = Result.index(min(Result))  # Определение разрешающего столбца
    value = matrix2[count][0] / matrix2[column][0]
    row = 0
    for y in range(q):  # Определение разрешающей строки
        p = matrix2[count][y] / matrix2[column][y]
        if p < value:
            value = p
            row = y

    resolution_element = matrix2[column][row]
    matrix2[column][row] = 1 / resolution_element  # Замена разрещающего символа

    for i in range(count + 1):  # Замена элементов не разрещающих
        for y in range(q):
            if y != row and i != column:
                matrix2[i][y] = matrix2[i][y] - (matrix2[column][y] * matrix2[i][row]) / resolution_element

    for i in range(count + 1):  # Замена элементов столбца
        if i != column:
            matrix2[i][row] = matrix2[i][row] / resolution_element

    for y in range(q):  # Замена элементов строки
        if y != row:
            matrix2[column][y] = -1 * (matrix2[column][y] / resolution_element)

    value = Cj[column]
    Cj[column] = Cb[row]
    Cb[row] = value

    value_char = Xj[column]
    Xj[column] = Xb[row]
    Xb[row] = value_char

    Result = []
    for i in range(count):  # Расчёт дельты
        r = 0
        for y in range(q):
            r += Cb[y] * matrix2[i][y]
        Result.append(r - Cj[i])

    for item in Result:  # Проверка на положительность дельты
        if item < 0:
            b = True

matrix3 = []
for i in range(1, count + q + 1):  # Вывод x
    if 'x' + str(i) in Xb:
        print('x' + str(i) + ' = ' + str(matrix2[-1][Xb.index('x' + str(i))]))
    else:
        print('x' + str(i) + ' = 0')

Q = 0
for i in range(q):
    Q += Cb[i] * matrix2[-1][i]

print('Q = ' + str(Q))