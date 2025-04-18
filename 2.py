try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
  
    result = num1 / num2
  
    print(f"Результат деления {num1} на {num2} равен {result}")
  
except ValueError:
    print("Ошибка: Введите числа!")

except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно!")

except Exception as e:
    print("Произошла ошибка: {e}")
