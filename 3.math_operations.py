def add(a, b):  # Cумма двух чисел
    return a + b

def subtract(a, b):   # Разность двух чисел
    return a - b

def multiply(a, b):   # Произведение двух чисел
    return a * b

def divide(a, b):     # Результат деления a на b.Выявление ошибки при деление на ноль
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b
