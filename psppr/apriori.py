# Транзакции
transactions = [
    ['Капуста', 'Перец', 'Кукуруза'],
    ['Спаржа', 'Кабачки', 'Кукуруза'],
    ['Кукуруза', 'Помидоры', 'Фасоль', 'Кабачки'],
    ['Перец', 'Кукуруза', 'Помидоры', 'Фасоль'],
    ['Фасоль', 'Спаржа', 'Капуста'],
    ['Кабачки', 'Спаржа', 'Фасоль', 'Помидоры'],
    ['Помидоры', 'Кукуруза'],
    ['Капуста', 'Помидоры', 'Перец'],
    ['Кабачки', 'Спаржа', 'Фасоль'],
    ['Фасоль', 'Кукуруза'],
    ['Перец', 'Капуста', 'Фасоль', 'Кабачки'],
    ['Спаржа', 'Фасоль', 'Кабачки'],
    ['Кабачки', 'Кукуруза', 'Спаржа', 'Фасоль'],
    ['Кукуруза', 'Перец', 'Помидоры', 'Фасоль', 'Капуста']
]

# Извлечение всех уникальных элементов из транзакций
unique_items = sorted(list(set(item for transaction in transactions for item in transaction)))

# Подсчет элементов в транзакциях
item_count = {item: 0 for item in unique_items}
for transaction in transactions:
    for item in transaction:
        item_count[item] += 1

# Определение порога
threshold = 5
frequent_items = {item: count for item, count in item_count.items() if count >= threshold}

# Генерация пар
pairs = [(a, b) for i, a in enumerate(unique_items) for b in unique_items[i+1:]]

# Подсчет пар в транзакциях
pair_count = {(a, b): 0 for a, b in pairs}
for transaction in transactions:
    for a, b in pairs:
        if a in transaction and b in transaction:
            pair_count[(a, b)] += 1

# Выбор часто встречающихся пар
frequent_pairs = {pair: count for pair, count in pair_count.items() if count >= threshold}

print("Frequent items:")
print(frequent_items)

print("Frequent pairs:")
print(frequent_pairs)
