import math_operations as mo

# Примеры использования функций из модуля
num1 = 18
num2 = 3

print(f"{num1} + {num2} = {mo.add(num1, num2)}")
print(f"{num1} - {num2} = {mo.subtract(num1, num2)}")
print(f"{num1} * {num2} = {mo.multiply(num1, num2)}")
print(f"{num1} / {num2} = {mo.divide(num1, num2)}")

# Проверка деления на ноль
print(f"{num1} / 0 = {mo.divide(num1, 0)}")
