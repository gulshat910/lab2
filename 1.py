import random

# Создаем файл data.txt с 10 случайными числами
with open('data.txt', 'w') as file:
    for _ in range(10):
        file.write(f"{random.randint(1, 100)}\n")

# Читаем числа из файла
with open('data.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Вычисляем результаты
sum_numbers = sum(numbers)
average = sum_numbers / len(numbers)
max_number = max(numbers)
min_number = min(numbers)

# Записываем результаты в файл result.txt
with open('result.txt', 'w') as file:
    file.write("Сумма: {sum_numbers}\n")
    file.write("Среднее: {average:}\n")
    file.write("Максимум: {max_number}\n")
    file.write("Минимум: {min_number}\n")

# Выводим результаты для наглядности
print("Результаты вычислений:")
print(f"Сумма: {sum_numbers}")
print(f"Среднее: {average:}")
print(f"Максимум: {max_number}")
print(f"Минимум: {min_number}")
print("\nРезультаты сохранены в файл result.txt")
