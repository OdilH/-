def remove_none(x):
    res = []
    for row in x:
        if row[0] is None:
            continue
        temp = []
        for cell in row:
            if cell is None:
                continue
            temp.append(cell)
        res.append(temp)
    return res


def remove_duplicates(x):
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def change_name(res):
    listOf = []
    for i in res:
        mail = i[0].split(";")[0].split("@")[0]
        phone = i[0].split(";")[1].split("(")[1].replace(")", "-")
        phone = phone[:10] + phone[11:]
        i[1] = int(i[1].split("%")[0]) / 100
        a = ('%.3f' % i[1])
        i[0] = phone
        i[1] = a
        i[2] = mail
        listOf.append(i)
    return listOf


def main(x):
    res = remove_none(x)
    res = remove_duplicates(res)
    res = change_name(res)
    return res
