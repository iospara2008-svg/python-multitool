# Python Multitool
if __name__ == "__main__":
    print("Programm works")


import time
import math_lib
import physics_lib
import tests


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
        print(eval(input()))


def executer():
    while True:
        exec(input())


def multitool_help():
    print("hello")


while True:
    match input().strip().lower():
        case "help":
            multitool_help()
        case "evaluater":
            evaluater()
        case "executer":
            executer()
        case _:
            print("undefined command")
