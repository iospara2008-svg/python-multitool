"""
Модуль physics_lib содержит следующие функции:
    физические формулы:
    расчет массы:
    1. def mass_formula(
    force=None,
    acceleration=None,
    m_1=None,
    m_2=None,
    distance=None,
    density=None,
    volume=None,
    amount_of_substance_in_moles=None,
    molar_mass=None,
    mass_of_one_molecule=None,
    number_of_particles=None,
    weight_force=None,
    total_energy_of_a_free_body=None,
    speed_of_light=None,
    impulse=None,
    force_gr=None,
    gravitational_constant=6.6743015 * pow(10, -11),
    acceleration_of_gravity=9.81,
    )->list
    расчет веса:
    2. weight_formula(mass, acceleration_of_gravity=9.81)->list
    расчет скорости:
    3. speed_formula(distance, time)->list
    расчет второй (освобожденной) космической скорости тела:
    4. the_second_liberation_cosmic_velocity_of_the_body_formula(
    radius_of_the_planet: float,
    orbit_altitude: float,
    orbital_speed: float,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float,
    gravitational_constant: float,
    )->list
    расчет закона Бойля - Мариотта:
    5. boyles_law_formula(gas_pressure: float, gas_volume: float)->list
    расчет закона Гей-Люссака:
    6. volumes_law_formula(gas_volume: float, temperature: float)->list
    расчет второго закона Гей-Люссака:
    7. gay_lussacs_second_law_formula(gas_pressure, temperature: float)->list
    расчет кинетической энергии тела:
    8. kinetic_energy_of_the_body_formula(mass: float, speed: float)->list
    расчет концентрации растворов:
    9. mixture_concentration_formula(
    component_mass: float, total_mass_of_all_components_of_the_mixture: float
    )->list
    расчет момента силы:
    10. moment_of_force_formula(force_module: float, shoulder_strength: float)->list
    расчет третьего закона Ньютона:
    11. newtons_third_law_formula(force_1: float)->list
    расчет молярной массы газа:
    12. molar_mass_of_gas_formula(
    mass_of_gas: float,
    amount_of_substance_in_moles: float,
    gas_density: float,
    density: float,
    universal_gas_constant: float,
    temperature_in_kelvin: float,
    pressure: float,
    molar_volume: float = 22.4,
    )->list
    расчет нормального ускорения при движении по окружности:
    13. normal_acceleration_when_moving_in_a_circle_formula(
    radius: float,
    speed: float,
    angular_velocity: float,
    )->list
    расчет ускорения:
    14. acceleration_formula(
    initial_speed: float,
    final_speed: float,
    time: float,
    force: float,
    mass: float,
    )->list
    return (final_speed - initial_speed) / time
    расчет первой (орбитальной) космической скорости тела:
    15. the_first_orbital_cosmic_velocity_of_a_body_formula(
    radius_of_the_planet: float,
    orbit_altitude: float,
    orbital_speed: float,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float,
    gravitational_constant: float,
    )->list
    расчет центробежной силы:
    16. centrifugal_force_formula(
    mass: float,
    speed: float,
    radius: float,
    angular_velocity: float,
    )->list
    расчет потенциальной энергии:
    17. potential_energy_formula(
    mass: float,
    acceleration_of_gravity: float,
    height: float,
    body_stiffness_coefficient: float,
    absolute_deformation: float,
    )->list
    расчет тангенциального ускорения:
    18. tangential_acceleration_formula(
    final_speed: float,
    initial_speed: float,
    delta_time: float,
    )->list
    расчет радиоактивного распада массы вещества через прошедшее время:
    19. mass_of_matter_over_time_formula(
    initial_number_of_cores: float,
    half_life: float,
    )->list
    расчет механической мощности:
    20. mechanic_power_formula(
    work: float,
    time: float,
    force: float,
    speed: float,
    torque: float,
    angular_velocity: float,
    )->list
    расчет постоянного тока:
    21. direct_current_formula(voltage: float, amperage: float, resist: float)->list
    расчет переменного тока:
    22. alternating_current_formula(
    voltage: float,
    amperage: float,
    active_power: float,
    reactive_power: float,
    )->list
    расчет силы:
    23. force_formula(mass: float, acceleration: float)->list
    расчет силы тока:
    24. amperage_formula(
    charge: float,
    time: float,
    voltage: float,
    resist: float,
    electrical_power: float,
    )->list
    расчет скорости звука:
    25. speed_of_sound_formula(
    adiabatic_compressibility_of_the_medium: float,
    medium_density: float,
    adiabatic_index: float,
    universal_gas_constant: float,
    absolute_temperature_in_Kelvin: float,
    molar_mass_of_gas: float,
    wavelength: float,
    oscillation_frequency: float,
    air_temperature_in_Celsius: float,
    )->list
    расчет третьей космической скорости тела:
    26. the_third_cosmic_velocity_of_a_body_formula(
    orbital_speed_of_the_planet: float,
    the_planets_second_cosmic_velocity: float,
    )->list
    расчет идеального газа:
    27. ideal_gas_formula(
    gas_pressure: float,
    gas_volume: float,
    absolute_temperature_in_kelvin: float,
    )->list
"""

import math
import json

# Физические константы
# Основные физические константы
physical_constant = """
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
|Quantity                           |Value      |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|elementary charge                  |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|Newtonian constant of gravitation  |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|Planck constant                    |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|speed of light in vacuum           |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|vacuum electric permittivity       |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|vacuum magnetic permeability       |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|electron mass                      |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|fine-structure constant            |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|Josephson constant                 |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|Rydberg constant                   |           |
|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!|
|von Klitzing constant              |           |
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

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
Energy_description = """
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
|Type of energy    |Description                                                     |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Chemical          |potential energy due to chemical bonds                          |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Chromodynamic     |potential energy that binds quarks to form hadrons              |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Elastic           |potential energy due to the deformation of a material           |
|                  |(or its container) exhibiting a restorative force as it         |
|                  |returns to its original shape                                   |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Electric          |potential energy due to or stored in electric fields            |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Gravitational     |potential energy due to or stored in electric fields            |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Ionization        |potential energy that binds an electron to its atom or molecule |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Magnetic          |potential energy due to or stored in magnetic fields            |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Mechanical        |the sum of macroscopic translational and rotational kinetic and |
|                  |potential energies                                              |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Mechanical wave   |kinetic and potential energy in an elastic material due to a    |
|                  |propagating oscillation of matter                               |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Nuclear           |kinetic and potential energy in an elastic material due to a    |
|                  |propagating oscillation of matter                               |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Radiant           |potential energy stored in the fields of waves propagated by    |
|                  |electromagnetic radiation, including light                      |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Rest              |potential energy due to an object's rest mass                   |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Rotational        |kinetic energy due to the rotation of an object                 |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Sound wave        |kinetic and potential energy in a material due to a sound       |
|                  |propagated wave (a particular type of mechanical wave)          |
|!!!!!!!!!!!!!!!!!!|!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!|
|Thermal           |kinetic energy of the microscopic motion of particles, a kind of|
|                  |disordered equivalent of mechanical energy                      |
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

with open("src/physics_data.json", "r") as _physics_data:
    physics_data = json.load(_physics_data)

print(physics_data)


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


def check(*args):
    for arg in args:
        if arg is None:
            return False
    return True


# распаковка величин в глобальные переменные для использования функциями
globals().update(physics_data["units"])


# Mass Inertial and Gravitational
# Масса - скалярная величина, определяющая инертные и гравитационные свойства тел.
# Масса эквивалентна энергии покоя
def mass_formula() -> list:  # Inertial mass
    results: list = []
    # print("force_gr = gravitational_constant * (m_1 * m_2) / distance^2")
    # return gravitational_constant * (m_1 * m_2) / pow(distance, 2)

    return results


def weight_formula() -> list:
    results: list = []

    return results


def speed_formula() -> list:
    results: list = []

    return results


def the_second_liberation_cosmic_velocity_of_the_body_formula() -> list:
    results: list = []

    return results


def boyles_law_formula() -> list:
    results: list = []

    return results


def volumes_law_formula() -> list:
    results: list = []

    return results


def kinetic_energy_of_the_body_formula() -> list:
    results: list = []

    return results


def mixture_concentration_formula() -> list:
    results: list = []

    return results


def moment_of_force_formula() -> list:
    results: list = []

    return results


def newtons_third_law_formula() -> list:
    results: list = []

    return results


def molar_mass_of_gas_formula() -> list:
    results: list = []

    return results


def normal_acceleration_when_moving_in_a_circle_formula() -> list:
    results: list = []

    return results


def acceleration_formula() -> list:
    results: list = []

    return results


def the_first_orbital_cosmic_velocity_of_a_body_formula() -> list:
    results: list = []

    return results


def centrifugal_force_formula() -> list:
    results: list = []

    return results


def potential_energy_formula() -> list:
    results: list = []

    return results


def tangential_acceleration_formula() -> list:
    results: list = []

    return results


def mass_of_matter_over_time_formula() -> list:
    results: list = []

    return results


def mechanic_power_formula() -> list:
    results: list = []

    return results


def direct_current_formula() -> list:
    results: list = []

    return results


def alternating_current_formula() -> list:
    results: list = []

    return results


def force_formula() -> list:
    results: list = []

    return results


def amperage_formula() -> list:
    results: list = []

    return results


def speed_of_sound_formula() -> list:
    results: list = []

    return results


def the_third_cosmic_velocity_of_a_body_formula() -> list:
    results: list = []

    return results


def ideal_gas_formula() -> list:
    results: list = []

    return results


if __name__ == "__main__":
    print("Module physics_lib is running")
    print(__doc__)
else:
    print(f"module is included: {__name__}")
