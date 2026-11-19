"""
Доступные команды:
    1. evaluater - оценивает вводимые выражения.
    Используйте evaluater для запуска и тестирования кода.

    2. executer - выполняет вводимый код.

Модули:
    Документация модуля хранится внутри модуля в переменной module_help.
    Для получения документации используйте "print(module_name.module_help)"
    с помощью "executer()".
"""

import time
from my_math import math_module
from my_physics import physics_module
# import tests

print("Python Multitool works")
print("Для получения помощи введите команду: help")


# Пример создания таймера _create_timer(ticks = 10, _action_func = func_name)
# Или _create_timer(ticks = 10, _action_func=lambda: print("hello"))
def create_timer(ticks, _action_func=None, _on_finish_func=None, period=1):
    while ticks > 0:
        if _action_func:
            _action_func()
        print(ticks)

        time.sleep(period)
        ticks -= 1

    if _on_finish_func:
        _on_finish_func()


def evaluater():
    while True:
        try:
            print(eval(input()))
        except (NameError, SyntaxError, AttributeError, TypeError, ValueError):
            print("Ошибка")
            print("Попробуйте снова")

def executer():
    while True:
        try:
            exec(input())
        except NameError, SyntaxError, AttributeError, TypeError, ValueError:
            print("Ошибка")
            print("Попробуйте снова")

while True:
    match input("user input ->").strip().lower():
        case "help":
            print(__doc__)
        case "evaluater":
            evaluater()
        case "executer":
            executer()
        case _:
            print("Неопределенная команда.")
