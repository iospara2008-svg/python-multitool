Python Multitool - инструмент предназначенный для решения математических, физических и других видов задач.

![Комару химик](stuff/komaru.png)

Правила написания кода:  
при написании кода в каждом модуле должен присутствовать этот паттерн в конце файла:

```python

module_help = "Текст документации модуля"

if __name__ == "__main__":
    print(f"Module {Название модуля} is running")
    print(module_help)
else:
    print(f"module is included: {__name__}")

# Пример
module_help = """
Модуль math_lib содержит следующие функции:
    формулы сокращенного умножения:
    1. square_of_sum_formula(a: float, b: float) -> float
    2. square_of_difference_formula(a: float, b: float) -> float
    3. difference_of_squares_formula(a: float, b: float) -> float
    4. difference_of_cubes_formula(a: float, b: float) -> float
    5. sum_of_cubes_formula(a: float, b: float) -> float
    6. cube_of_sum_formula(a: float, b: float) -> float
    7. difference_of_cube_formula(a: float, b: float) -> float
    формула квадратного уравнения:
    8. quadratic_equation_formula(a: float, b: float, c: float) -> float
    формула факториала:
    9. factorial_formula(n: float) -> float
"""

if __name__ == "__main__":
    print("Module math_lib is running")
    print(module_help)
else:
    print(f"module is included: {__name__}")
```

Названием модуля является название файла.  
Это нужно для проверки подключенных модулей к запускаемому коду и получение документации по модулю при его запуске или через переменную ```module_help```.
