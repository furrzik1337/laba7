# Ввод списка вещественных чисел
numbers = list(map(float, input("Введите элементы списка через пробел: ").split()))

# 1. Номер минимального элемента списка
min_value = min(numbers)
min_index = numbers.index(min_value) + 1  # индекс начинаем с 1

# 2. Сумма элементов между первым и вторым отрицательными элементами
negative_indices = [i for i, x in enumerate(numbers) if x < 0]

if len(negative_indices) >= 2:
    first_negative = negative_indices[0]
    second_negative = negative_indices[1]
    sum_between = sum(numbers[first_negative + 1:second_negative])
else:
    sum_between = 0

# Вывод результатов
print(f"Номер минимального элемента: {min_index}")
print(f"Сумма элементов между первым и вторым отрицательными элементами: {sum_between}")
