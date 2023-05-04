x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = x[8::-2]
b = x[1::2]
c = []

for i, j in zip(a, b):
    c.append(i)
    c.append(j)

print(c)

