transactions = [['11111', 'Слива', 'Салат', 'Помидоры'],
                ['12222', 'Сельдерей', 'Конфеты'],
                ['13333', 'Конфеты'],
                ['14444', 'Яблоки', 'Морковь', 'Помидоры', 'Картофель', 'Конфеты'],
                ['15555', 'Яблоки', 'Апельсины', 'Салат', 'Конфеты', 'Помидоры'],
                ['16666', 'Персики', 'Сельдерей', 'Помидоры'],
                ['17777', 'Фасоль', 'Салат', 'Помидоры'],
                ['18888', 'Апельсин', 'Салат', 'Морковь', 'Помидоры', 'Конфеты'],
                ['19999', 'Яблоки', 'Бананы', 'Сливы', 'Морковь', 'Помидоры', 'Конфеты', 'Лук'],
                ['10000', 'Яблоки', 'Картофель']
                ]

# Calculate the frequency of items in transactions
item_counts = {}
for transaction in transactions:
    for item in transaction:
        if item not in item_counts:
            item_counts[item] = 1
        else:
            item_counts[item] += 1

# Calculate the number of transactions
transaction_count = len(transactions)

# Calculate the support for each item
support = {}
for item, count in item_counts.items():
    support[item] = count / transaction_count

# Calculate the confidence for each item
confidence = {}
for transaction in transactions:
    for item in item_counts:
        if item in transaction:
            if item not in confidence:
                confidence[item] = {}
            for other_item in item_counts:
                if other_item != item and other_item in transaction:
                    if other_item not in confidence[item]:
                        confidence[item][other_item] = 0
                    confidence[item][other_item] += 1

for item, related_items in confidence.items():
    item_support = support[item]
    for related_item, count in related_items.items():
        confidence[item][related_item] = count / item_support

# Calculate the lift for each item
lift = {}
for item, related_items in confidence.items():
    for related_item, confidence_value in related_items.items():
        if item not in lift:
            lift[item] = {}
        lift[item][related_item] = confidence_value / support[related_item]


print("Поддержка:")
for item, support_value in support.items():
    print("\t{}: {:.2f}".format(item, support_value))

print("\nДостоверность:")
for item, related_items in confidence.items():
    for related_item, confidence_value in related_items.items():
        print("\t{} -> {}: {:.2f}".format(item, related_item, confidence_value))

print("\nЛифт:")
for item, related_items in lift.items():
    for related_item, lift_value in related_items.items():
        print("\t{} -> {}: {:.2f}".format(item, related_item, lift_value))
