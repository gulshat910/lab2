numbers = list(range(1, 21))

# 1. Фильтрация чётных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 2. Увеличение каждого числа на 10
increased_numbers = list(map(lambda x: x + 10, numbers))

# 3. Сортировка по убыванию
sorted_numbers = sorted(numbers, key=lambda x: -x)

# Вывод результатов
print("Исходный список:", numbers)
print("Чётные числа:", even_numbers)
print("Числа +10:", increased_numbers)
print("Сортировка по убыванию:", sorted_numbers)
