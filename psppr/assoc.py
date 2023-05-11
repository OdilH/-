from collections import defaultdict
from itertools import combinations, chain


def itemsets_frequency(transactions):
    frequency = defaultdict(int)
    for transaction in transactions:
        for itemset in chain(*[combinations(transaction, i + 1) for i, _ in enumerate(transaction)]):
            frequency[itemset] += 1
    return frequency


def association_rules(transactions, min_support=0, min_confidence=0):
    frequency = itemsets_frequency(transactions)
    transaction_num = len(transactions)

    itemset_keys = list(frequency.keys())
    for itemset in itemset_keys:
        support = frequency[itemset] / transaction_num
        if support < min_support:
            continue

        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(itemset) - set(antecedent)))
                if len(antecedent) == 0 or len(consequent) == 0:
                    continue

                if frequency[antecedent] == 0:
                    continue

                confidence = frequency[itemset] / frequency[antecedent]
                if confidence < min_confidence:
                    continue

                if frequency[consequent] == 0:
                    continue

                lift = confidence / (frequency[consequent] / transaction_num)

                yield (antecedent, consequent, support, confidence, lift)


transactions = [['Слива', 'Салат', 'Помидоры'],
                ['Сельдерей', 'Конфеты'],
                ['Конфеты'],
                ['Яблоки', 'Морковь', 'Помидоры', 'Картофель', 'Конфеты'],
                ['Яблоки', 'Апельсины', 'Салат', 'Конфеты', 'Помидоры'],
                ['Персики', 'Сельдерей', 'Помидоры'],
                ['Фасоль', 'Салат', 'Помидоры'],
                ['Апельсин', 'Салат', 'Морковь', 'Помидоры', 'Конфеты'],
                ['Яблоки', 'Бананы', 'Сливы', 'Морковь', 'Помидоры', 'Конфеты', 'Лук'],
                ['Яблоки', 'Картофель']
                ]

rules = list(association_rules(transactions, min_support=0.2, min_confidence=0.6))
for rule in rules:
    print(f"Правило: {rule[0]} => {rule[1]}, Поддержка: {rule[2]}, Достоверность: {rule[3]}, Лифт: {rule[4]}")
