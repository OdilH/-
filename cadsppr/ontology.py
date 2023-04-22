class CEO:
    def __init__(self, birth, salary, phone, late, overwork, exp, fio, subord):
        self.birth = birth
        self.salary = salary
        self.phone = phone
        self.late = late
        self.overwork = overwork
        self.exp = exp
        self.fio = fio
        self.subord = subord

    def __str__(self):
        return "Руководитель: " + str(self.fio)


class Fin_Otdel:
    def __init__(self, birth, salary, phone, late, overwork, exp, fio):
        self.birth = birth
        self.salary = salary
        self.phone = phone
        self.late = late
        self.overwork = overwork
        self.exp = exp
        self.fio = fio


class Clients:
    def __init__(self, birth, salary, phone, late, overwork, exp, fio):
        self.birth = birth
        self.salary = salary
        self.phone = phone
        self.late = late
        self.overwork = overwork
        self.exp = exp
        self.fio = fio


class Financist(Fin_Otdel):
    def __str__(self):
        return "Финансист: " + str(self.fio)


class Broker(Fin_Otdel):
    def __str__(self):
        return "Брокер: " + str(self.fio)


class Buhgalter(CEO, Fin_Otdel):
    def __str__(self):
        return "Бухгалтер: " + str(self.fio)


class Cashier(Clients):
    def __init__(self, birth, salary, phone, late, overwork, exp, fio, kassa):
        super().__init__(birth, salary, phone, late, overwork, exp, fio)
        self.kassa = kassa

    def __str__(self):
        return "Кассир: " + str(self.fio)


class Consultant(Clients):
    def __str__(self):
        return "Консультант: " + str(self.fio)


class Manager(CEO, Clients):
    def __str__(self):
        return "Менеджер: " + str(self.fio)


class Director(CEO):
    def __str__(self):
        return "Директор: " + str(self.fio)


if __name__ == "__main__":
    staff = []
    staff.append(Financist("22.05.2002", 100000.0, "222-222-22", "1 час", "0", "5 лет", "Финанс Ф.Ф."))
    staff.append(Financist("22.05.2002", 102000.0, "222-222-22", "1 час", "0", "5 лет", "Финанс2 Ф.Ф."))
    staff.append(Broker("6.04.1999", 150000.0, "333-333-33", "1 час", "4 часа", "4 года", "Брокер Б.Б."))
    staff.append(Broker("6.04.1999", 151000.0, "333-333-33", "1 час", "4 часа", "4 года", "Брокер1 Б.Б."))
    staff.append(Buhgalter("9.12.1800", 80000.0, "888-888-88", "0", "0", "10 лет", "Галтер Г.Г.",
                           [staff[0], staff[1], staff[2], staff[3]]))
    staff.append(Cashier("30.03.1990", 100000.0, "800-555-35", "5 часов", "10 часов", "1 год", "Касса К.К.", 5))
    staff.append(Cashier("30.03.1990", 100100.0, "800-555-35", "5 часов", "10 часов", "1 год", "Касса1 К.К.", 6))
    staff.append(Consultant("6.04.1901", 123000.0, "444-444-44", "0", "0", "8 лет", "Консуль К.К."))
    staff.append(Consultant("6.04.1901", 123200.0, "444-444-44", "0", "0", "8 лет", "Консуль2 К.К."))

    staff.append(Manager("12.03.1456", 123456.0, "666-666-66", "0", "7 часов", "9 лет", "Менедж М.М.",
                         [staff[5], staff[6], staff[7], staff[8]]))
    staff.append(
        Director("11.11.1111", 200000.0, "111-111-11", "0", "0", "1 год", "Директор Д.Д.", [staff[4], staff[9]]))
    staff.append(
        CEO("1.01.2000", 1000000.0, "000-000-00", "0", "5 часов", "10 лет", "Глава Г.Г.",
            [staff[4], staff[9], staff[10]]))
while (True):
    print("Выберите класс:")
    print("1. Руководитель")
    print("2. Финансист")
    print("3. Брокер")
    print("4. Бухгалтер")
    print("5. Кассир")
    print("6. Консультант")
    print("7. Менеджер")
    print("8. Директор")
    print("9. Фин. Отдел")
    print("10. Отдел по работе с клиентами")
    i = int(input())
    cl = 0
    if i == 1:
        cl = CEO
    elif i == 2:
        cl = Financist
    elif i == 3:
        cl = Broker
    elif i == 4:
        cl = Buhgalter
    elif i == 5:
        cl = Cashier
    elif i == 6:
        cl = Consultant
    elif i == 7:
        cl = Manager
    elif i == 8:
        cl = Director
    elif i == 9:
        cl = Fin_Otdel
    elif i == 10:
        cl = Clients

    if cl == 0:
        continue
    print("Выберите атрибут:")
    print("1. ФИО")
    print("2. Дата рождения")
    print("3. Зарплата")
    print("4. Телефон")
    print("5. Переработка")
    print("6. Опоздание")
    print("7. Опыт работы")
    if cl == Cashier:
        print("8. Касса")
    elif cl == CEO or cl == Director or cl == Buhgalter or cl == Manager:
        print("8. Подчиненные")
    i = int(input())
    at = 0
    if i == 1:
        at = "fio"
    elif i == 2:
        at = "birth"
    elif i == 3:
        at = "salary"
    elif i == 4:
        at = "phone"
    elif i == 5:
        at = "overwork"
    elif i == 6:
        at = "late"
    elif i == 7:
        at = "exp"
    elif i == 8:
        if cl == Cashier:
            at = "kassa"
        elif cl == CEO or cl == Director or cl == Buhgalter or cl == Manager:
            at = "subord"
    if at == 0:
        continue
    print("Выберите условие:")
    usl = 0
    if at == "kassa" or at == "salary":
        print("1. Больше")
        print("2. Меньше")
        print("3. Равно")
        print("4. Неравно")
    i = int(input())
    if i == 1:
        usl = ">"
    elif i == 2:
        usl = "<"
    elif i == 3:
        usl = "="
    elif i == 4:
        usl = "!="
    elif at == "subord":
        print("1. Есть")
    print("2. Нет")
    i = int(input())
    if i == 1:
        usl = "yes"
    elif i == 2:
        usl = "no"
    else:
        print("1. Содержит")
    print("2. Не содержит")
    i = int(input())
    if i == 1:
        usl = "in"
    elif i == 2:
        usl = "not in"
    if usl == 0:
        continue
    print("Укажите параметр поиска:")
    par = 0
    if at == "kassa" or at == "salary":
        par = int(input())
    elif at == "subord":
        for i in range(len(staff)):
            print(i + 1, str(staff[i]))
        par = int(input())
        par = staff[par - 1]

    else:
        par = input()
    for i in range(len(staff)):
        if isinstance(staff[i], cl):
            if at == "subord":
                testn = True
    for q in range(len(staff[i].subord)):
        if staff[i].subord[q] == par and usl == "yes":
            print(staff[i])
            break
        elif usl == "no" and staff[i].subord[q] == par:
            testn = False
        if usl == "no" and testn:
            print(staff[i])
        else:
            a = getattr(staff[i], at)
            if usl == ">":
                if a > par:
                    print(staff[i])
            elif usl == "<":
                if a < par:
                    print(staff[i])
            elif usl == "=":
                if a == par:
                    print(staff[i])
            elif usl == "!=":
                if a != par:
                    print(staff[i])
            elif usl == "in":
                if a.find(par) >= 0:
                    print(staff[i])
            elif usl == "not in":
                if a.find(par) == -1:
                    print(staff[i])
