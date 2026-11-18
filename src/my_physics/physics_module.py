"""
physics_module

Создание физического объекта:
create_physical_object(name_of_physical_object: str)

вывод величин физического элемента:
print_values(name_of_physical_object: str)

нахождение величины физического объекта по названию:
find_value(name_of_physical_object, name_of_value, accept)

Модуль содержит следующие физические формулы:
    расчет массы
    расчет веса
    расчет скорости
    расчет второй (освобожденной) космической скорости тела
    расчет закона Бойля - Мариотта
    расчет закона Гей-Люссака
    расчет второго закона Гей-Люссака
    расчет кинетической энергии тела
    расчет концентрации растворов
    расчет момента силы
    расчет третьего закона Ньютона
    расчет молярной массы газа
    расчет нормального ускорения при движении по окружности
    расчет ускорения
    расчет первой (орбитальной) космической скорости тела
    расчет центробежной силы
    расчет потенциальной энергии
    расчет тангенциального ускорения
    расчет радиоактивного распада массы вещества через прошедшее время
    расчет механической мощности
    расчет постоянного тока
    расчет переменного тока
    расчет силы
    расчет силы тока
    расчет скорости звука
    расчет третьей космической скорости тела
    расчет идеального газа
"""

import math
import json

with open("src/my_physics/Physics_data", "r") as _physics_data:
    physics_data = json.load(_physics_data)

physical_objects: dict = {}


# Физические константы
# Основные физические константы
physical_constant = physics_data["tables"]["physical_constant"]

# Вещества
# Вещество может иметь агрегатные состояния: твердое; жидкое; газообразное; плазма; сверхтекучее; сверхпроводящее.
# Помимо этого также существуют такие состаяния как аморфное (стеклообразное) состояние, состояние жидкого кристалла и высокоэластичное (полимерное) состояние.
# Вещество может сжиматься и расширяться или изменять агрегатное состояние.
# Их можно смешивать, получая новые вещества.

# Набор специфических свойств вещества:
# Constants:
# density  # Плотность
# melting_point  # Температура плавления
# boiling_point  # Температура кипения
# thermodynamic_characteristics  # Термодинамические характеристики
# crystal_structure_parameters  # Кристалическая структура
# chemical_properties.  # Химические свойствa


# Время
# Время необратимо.
# Атомное время измеряется в 9 192 631 770 периодов излучения цезия-133 при отсутствии возмущения внешними полями что равно 1 секунде.


# Энергия
# Скаляраная физическая величина, являющаяся единой мерой различных форм движения и взаимодействия материи.
# если физическая система является замкнутой, то её энергия сохраняется в этой системе на протяжении времени, в течение которого система будет являться замкнутой. Это называется законом сохранения энергии.
energy_description = physics_data["tables"]["energy_description"]


# пример создание объекта наследуемого от класса UnitBase: object_mass = _Mass(value, "kilogram")
class UnitBase:
    # Создание объекта (экземлпяра класса), инициализация принимает аргументы: Количество что является произвольной величиной
    # не зависящей от единицы измерения и название единицы измерения для ее определения
    def __init__(self, value: float, dimension: str):
        dimension = dimension.lower()

        # преобразование value в соответствии с переданным аргументом _dimension.
        self.value = value
        self.dimension = dimension

    # Функция для преобразования единиц измерения принимает аргумент
    # единица измерения to_dimension в которую нужно преобразовать величину (переменную value).
    def convert(self, to_dimension: str):
        to_dimension = to_dimension.lower()

        # преобразование value в соответствии с переданным аргументом to_dimension.
        self.value = self.value * self.dimensions[self.dimension]
        self.value = self.value / self.dimensions[to_dimension]
        self.dimension = to_dimension

    value: float
    dimension: str

    def __str__(self):
        return f"Value {self.value}, Dimension {self.dimension}"


class Time(UnitBase):
    dimensions = physics_data["unit_dimensions"]["time_dimensions"]


class Distance(UnitBase):
    dimensions = physics_data["unit_dimensions"]["distance_dimensions"]


class Mass(UnitBase):
    dimensions = physics_data["unit_dimensions"]["mass_dimensions"]


class Pressure(UnitBase):
    dimensions = physics_data["unit_dimensions"]["pressure_dimensions"]


class Volume(UnitBase):
    dimensions = physics_data["unit_dimensions"]["volume_dimensions"]


class PlaneAngle(UnitBase):
    dimensions = physics_data["unit_dimensions"]["plane_angle_dimensions"]


class Area(UnitBase):
    dimensions = physics_data["unit_dimensions"]["area_dimensions"]


# Этот класс писала нейронка
class FuelConsumption(UnitBase):
    dimensions = physics_data["unit_dimensions"]["fuel_consumption_dimensions"]

    def convert(self, to_dimension: str):
        to_dimension = to_dimension.lower()

        # 1. Сначала переводим текущее значение к базовому "liter_per_100_km"
        if self.dimension == "us_mpg":
            # Перевод из US MPG в л/100 км: 235.214583 / mpg
            base_value = 235.214583 / self.value
        elif self.dimension == "imperial_mpg":
            # Перевод из Imperial MPG в л/100 км: 282.480936 / imperial_mpg
            base_value = 282.480936 / self.value
        elif self.dimension == "kilometer_per_liter":
            # Перевод из км/л в л/100 км: 100 / km_per_l
            base_value = 100.0 / self.value
        else:
            base_value = self.value  # уже liter_per_100_km

        # 2. Теперь из базового "liter_per_100_km" переводим в целевую единицу to_dimension
        if to_dimension == "us_mpg":
            new_value = 235.214583 / base_value if base_value > 0 else 0
        elif to_dimension == "imperial_mpg":
            new_value = 282.480936 / base_value if base_value > 0 else 0
        elif to_dimension == "kilometer_per_liter":
            new_value = 100.0 / base_value if base_value > 0 else 0
        else:
            new_value = base_value  # liter_per_100_km

        # Обновляем значения
        self.value = new_value
        self.dimension = to_dimension


# Этот класс писала нейронка
class Speed(UnitBase):
    dimensions = physics_data["unit_dimensions"]["speed_dimensions"]


class Frequency(UnitBase):
    dimensions = physics_data["unit_dimensions"]["frequency_dimensions"]


class Energy(UnitBase):
    dimensions = physics_data["unit_dimensions"]["energy_dimensions"]


# Этот класс писала нейронка
class Temperature(UnitBase):
    # В качестве базы держим celsius
    dimensions = physics_data["unit_dimensions"]["temperature_dimensions"]

    def convert(self, to_dimension: str):
        to_dimension = to_dimension.lower()
        if not hasattr(self, to_dimension):
            raise ValueError(f"Unknown dimension: {to_dimension}")

        # 1. Сначала переводим текущее значение к базовому "celsius"
        if self.dimension == "fahrenheit":
            # Перевод из Fahrenheit в Celsius: (F - 32) * 5 / 9
            base_value = (self.value - 32) * 5 / 9
        elif self.dimension == "kelvin":
            # Перевод из Kelvin в Celsius: K - 273.15
            base_value = self.value - 273.15
        else:
            base_value = self.value  # уже celsius

        # 2. Теперь из базового "celsius" переводим в целевую единицу to_dimension
        if to_dimension == "fahrenheit":
            new_value = (base_value * 9 / 5) + 32
        elif to_dimension == "kelvin":
            new_value = base_value + 273.15
        else:
            new_value = base_value  # celsius

        # Обновляем флаги и значения
        setattr(self, self.dimension, False)
        setattr(self, to_dimension, True)
        self.value = new_value
        self.dimension = to_dimension

    # Нужно написать отдельный конвертер для температуры


# создание физического объекта
def create_physical_object(name_of_physical_object: str):
    values = physics_data["units"]
    formulas = physics_data["formulas"]
    physical_objects[name_of_physical_object] = {"values": values, "formulas": formulas}

def print_values(name_of_physical_object: str):
    for value in physical_objects[name_of_physical_object["values"]]:
        print(value)

# нахождение любого значения
def find_value(name_of_physical_object, name_of_value, accept):
    for formula in physical_objects[name_of_physical_object]["formulas"]:
        try:
            ansver = eval(formula)  # исполняем код вычисляющий значение
            if accept:
                physical_objects[name_of_physical_object]["values"] = ansver
        except TypeError:
            print(f"error: {formula}, возможно переменная из формулы неопределена")
        finally:
            print(f"ansver: {ansver}")
    print(
        f"name of value: {name_of_value}, value:{physics_data['units'][name_of_value]}"
    )


if __name__ == "__main__":
    print("Module physics_lib is running")
    print(__doc__)
else:
    print(f"module is included: {__name__}")
