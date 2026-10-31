import math

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


# пример создание объекта наследуемого от класса unit_base: object_mass = _Mass(value, "kilogram")
class unit_base:
    # Создание объекта (экземлпяра класса), инициализация принимает аргументы: Количество что является произвольной величиной
    # не зависящей от единицы измерения и название единицы измерения для ее определения
    def __init__(self, value: float, dimension: str):
        dimension = dimension.lower()

        if hasattr(self, dimension):  # если класс имеет арибут совпадающий с
            setattr(self, dimension, True)  # названием переданного аргумента
            # то атрибуту присваивается значение True.

            # преобразование value в соответствии с переданным аргументом _dimension.
            self.value = value
            self.dimension = dimension

    # Функция для преобразования единиц измерения принимает аргумент
    # единица измерения to_dimension в которую нужно преобразовать величину (переменную value).
    def convert(self, to_dimension: str):
        to_dimension = to_dimension.lower()

        # Сброс флага dimension для назначения нового to_dimension.
        setattr(self, self.dimension, False)
        setattr(self, to_dimension, True)

        # преобразование value в соответствии с переданным аргументом to_dimension.
        self.value = self.value * self.dimensions[self.dimension]
        self.value = self.value / self.dimensions[to_dimension]
        self.dimension = to_dimension

    value: float
    dimension: str

    def __str__(self):
        return f"Value {self.value}, Dimension {self.dimension}"


class Time(unit_base):
    nanosecond: bool = False
    microsecond: bool = False
    millisecond: bool = False
    second: bool = False
    minute: bool = False
    hour: bool = False
    day: bool = False
    week: bool = False
    year: bool = False
    century: bool = False
    exasecond: bool = False

    dimensions = {
        "nanosecond": 1e9,
        "microsecond": 1e6,
        "millisecond": 1e3,
        "second": 1,
        "minute": 60,
        "hour": 60 * 60,
        "day": 60 * 60 * 24,
        "week": 60 * 60 * 24 * 7,
        "year": 60 * 60 * 24 * 365,
        "century": 60 * 60 * 24 * 365 * 100,
        "exasecond": 1e18,
    }


class Distance(unit_base):
    nanometer: bool = False
    micrometer: bool = False
    millimeter: bool = False
    centimeter: bool = False
    decimeter: bool = False
    meter: bool = False
    kilometer: bool = False
    inch: bool = False
    foot: bool = False
    yard: bool = False
    mile: bool = False
    nautical_mile: bool = False
    planck_length: bool = False

    dimensions = {
        "nanometer": 1e-9,
        "micrometer": 1e-6,
        "millimeter": 1e-3,
        "centimeter": 1e-2,
        "decimeter": 1e-1,
        "meter": 1,
        "kilometer": 1e3,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
        "nautical_mile": 1852,
        "planck_length": 1.616e-35,
    }


class Mass(unit_base):
    microgram: bool = False
    milligram: bool = False
    gram: bool = False
    kilogram: bool = False
    centner: bool = False
    ton: bool = False
    pound: bool = False
    ounce: bool = False
    carat: bool = False

    dimensions = {
        "microgram": 1e-6,
        "milligram": 1e-3,
        "gram": 1.0,
        "kilogram": 1e3,
        "centner": 1e5,
        "ton": 1e6,
        "pound": 453.59237,
        "ounce": 28.3495231,
        "carat": 0.2,
    }


class Pressure(unit_base):
    atmosphere: bool = False
    bar: bool = False
    pascal: bool = False
    torr: bool = False
    pound_force_per_square_inch: bool = False

    dimensions = {
        "pascal": 1,
        "bar": 100000.0,
        "atmosphere": 101325.0,
        "torr": 133.322,
        "pound_force_per_square_inch": 6894.76,
    }


class Volume(unit_base):
    liter: bool = False
    cubic_meter: bool = False
    milliliter: bool = False
    us_gallon: bool = False
    us_liquid_quart: bool = False
    us_liquid_pint: bool = False
    us_cup: bool = False
    us_fluid_ounce: bool = False
    us_tablespoon: bool = False
    us_teaspoon: bool = False
    imperial_gallon: bool = False
    imperial_quart: bool = False
    imperial_pint: bool = False
    imperial_cup: bool = False
    imperial_fluid_ounce: bool = False
    british_tablespoon: bool = False
    british_teaspoon: bool = False
    cubic_foot: bool = False
    cubic_inch: bool = False

    dimensions = {
        "liter": 1.0,
        "cubic_meter": 1000.0,
        "milliliter": 0.001,
        "us_gallon": 3.78541,
        "us_liquid_quart": 0.946353,
        "us_liquid_pint": 0.473176,
        "us_cup": 0.24,
        "us_fluid_ounce": 0.0295735,
        "us_tablespoon": 0.0147868,
        "us_teaspoon": 0.00492892,
        "imperial_gallon": 4.54609,
        "imperial_quart": 1.13652,
        "imperial_pint": 0.568261,
        "imperial_cup": 0.284131,
        "imperial_fluid_ounce": 0.0284131,
        "british_tablespoon": 0.0177582,
        "british_teaspoon": 0.00591939,
        "cubic_foot": 28.3168,
        "cubic_inch": 0.0163871,
    }


# надо будет перенести этот класс в отдельный модуль
class DataStorage(unit_base):
    bit: bool = False
    kilobit: bool = False
    kibibit: bool = False
    megabit: bool = False
    mebibit: bool = False
    gigabit: bool = False
    gibibit: bool = False
    terabit: bool = False
    tebibit: bool = False
    petabit: bool = False
    pebibit: bool = False
    byte: bool = False
    kilobyte: bool = False
    kibibyte: bool = False
    megabyte: bool = False
    mebibyte: bool = False
    gigabyte: bool = False
    gibibyte: bool = False
    terabyte: bool = False
    tebibyte: bool = False
    petabyte: bool = False
    pebibyte: bool = False

    dimensions = {
        "bit": 1.0,
        "byte": 8.0,
        "kilobit": 1000.0,
        "kibibit": 1024.0,
        "megabit": 1_000_000.0,
        "mebibit": 1_048_576.0,
        "gigabit": 1_000_000_000.0,
        "gibibit": 1_073_741_824.0,
        "terabit": 1_000_000_000_000.0,
        "tebibit": 1_099_511_627_776.0,
        "petabit": 1_000_000_000_000_000.0,
        "pebibit": 1_125_899_906_842_624.0,
        "kilobyte": 8000.0,
        "kibibyte": 8192.0,
        "megabyte": 8_000_000.0,
        "mebibyte": 8_388_608.0,
        "gigabyte": 8_000_000_000.0,
        "gibibyte": 8_589_934_592.0,
        "terabyte": 8_000_000_000_000.0,
        "tebibyte": 8_796_093_022_208.0,
        "petabyte": 8_000_000_000_000_000.0,
        "pebibyte": 9_007_199_254_740_992.0,
    }


class PlaneAngle(unit_base):
    degree: bool = False
    gradian: bool = False
    minute_of_arc: bool = False
    radian: bool = False
    mil: bool = False
    second_of_arc: bool = False

    dimensions = {
        "radian": 1.0,
        "degree": 0.017453292519943295,  # pi / 180
        "gradian": 0.015707963267948967,  # pi / 200
        "minute_of_arc": 0.0002908882086657216,  # pi / 10800
        "second_of_arc": 0.00000484813681109536,  # pi / 648000
        "mil": 0.0009817477042468103,  # приближенно (обычно военный тысячный / NATO mil)
    }


class Area(unit_base):
    square_meter: bool = False
    square_kilometer: bool = False
    square_mile: bool = False
    square_yard: bool = False
    square_foot: bool = False
    square_inch: bool = False
    hectare: bool = False
    acre: bool = False

    dimensions = {
        "square_meter": 1.0,
        "square_kilometer": 1_000_000.0,
        "square_mile": 2_589_988.110336,
        "square_yard": 0.83612736,
        "square_foot": 0.09290304,
        "square_inch": 0.00064516,
        "hectare": 10_000.0,
        "acre": 4046.8564224,
    }


# Этот класс писала нейронка
class FuelConsumption(unit_base):
    liter_per_100_km: bool = False
    kilometer_per_liter: bool = False
    us_mpg: bool = False
    imperial_mpg: bool = False

    # В качестве базы держим liter_per_100_km
    dimensions = {
        "liter_per_100_km": 1.0,
    }

    def convert(self, to_dimension: str):
        to_dimension = to_dimension.lower()
        if not hasattr(self, to_dimension):
            raise ValueError(f"Unknown dimension: {to_dimension}")

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

        # Обновляем флаги и значения
        setattr(self, self.dimension, False)
        setattr(self, to_dimension, True)
        self.value = new_value
        self.dimension = to_dimension


# Этот класс писала нейронка
class Speed(unit_base):
    meter_per_second: bool = False
    kilometer_per_hour: bool = False
    mile_per_hour: bool = False
    foot_per_second: bool = False
    knot: bool = False

    dimensions = {
        "meter_per_second": 1.0,
        "kilometer_per_hour": 0.2777777778,  # 1 км/ч = 1 / 3.6 м/с
        "mile_per_hour": 0.44704,  # 1 mph = 0.44704 м/с
        "foot_per_second": 0.3048,  # 1 ft/s = 0.3048 м/с
        "knot": 0.514444,  # 1 узел = 0.514444 м/с
    }


# надо будет перенести этот класс в отдельный модуль
class DataTransferRate(unit_base):
    bit_per_second: bool = False
    kilobit_per_second: bool = False
    kibibit_per_second: bool = False
    megabit_per_second: bool = False
    mebibit_per_second: bool = False
    gigabit_per_second: bool = False
    gibibit_per_second: bool = False
    terabit_per_second: bool = False
    tebibit_per_second: bool = False
    byte_per_second: bool = False
    kilobyte_per_second: bool = False
    kibibyte_per_second: bool = False
    megabyte_per_second: bool = False
    mebibyte_per_second: bool = False
    gigabyte_per_second: bool = False
    gibibyte_per_second: bool = False
    terabyte_per_second: bool = False
    tebibyte_per_second: bool = False

    dimensions = {
        "bit_per_second": 1.0,
        "byte_per_second": 8.0,
        "kilobit_per_second": 1000.0,
        "kibibit_per_second": 1024.0,
        "megabit_per_second": 1_000_000.0,
        "mebibit_per_second": 1_048_576.0,
        "gigabit_per_second": 1_000_000_000.0,
        "gibibit_per_second": 1_073_741_824.0,
        "terabit_per_second": 1_000_000_000_000.0,
        "tebibit_per_second": 1_099_511_627_776.0,
        "kilobyte_per_second": 8000.0,
        "kibibyte_per_second": 8192.0,
        "megabyte_per_second": 8_000_000.0,
        "mebibyte_per_second": 8_388_608.0,
        "gigabyte_per_second": 8_000_000_000.0,
        "gibibyte_per_second": 8_589_934_592.0,
        "terabyte_per_second": 8_000_000_000_000.0,
        "tebibyte_per_second": 8_796_093_022_208.0,
    }


class Frequency(unit_base):
    hertz: bool = False
    kilohertz: bool = False
    megahertz: bool = False
    gigahertz: bool = False

    dimensions = {
        "hertz": 1.0,
        "kilohertz": 1e3,
        "megahertz": 1e6,
        "gigahertz": 1e9,
    }


class Energy(unit_base):
    joule: bool = False
    kilojoule: bool = False
    gram_calorie: bool = False
    kilocalorie: bool = False
    watt_hour: bool = False
    kilowatt_hour: bool = False
    electronvolt: bool = False
    british_thermal_unit: bool = False
    us_therm: bool = False
    foot_pound: bool = False

    dimensions = {
        "joule": 1.0,
        "kilojoule": 1e3,
        "gram_calorie": 4.184,
        "kilocalorie": 4.184e3,
        "watt_hour": 3.6e3,
        "kilowatt_hour": 3.6e6,
        "electronvolt": 1.602176634e-19,
        "british_thermal_unit": 1055.05585262,
        "us_therm": 1.054804e8,
        "foot_pound": 1.3558179483314004,
    }


# Этот класс писала нейронка
class Temperature(unit_base):
    celsius: bool = False
    fahrenheit: bool = False
    kelvin: bool = False

    # В качестве базы держим celsius
    dimensions = {
        "celsius": 1.0,
        "fahrenheit": 1.0,
        "kelvin": 1.0,
    }

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


# Mass Inertial and Gravitational
# Масса - скалярная величина, определяющая инертные и гравитационные свойства тел.
# Масса эквивалентна энергии покоя
def mass_formula(
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
) -> float:  # Inertial mass
    if force is not None and acceleration is not None:
        print("force = mass * acceleration -> mass = force / acceleration")
        return force / acceleration
    if (
        force_gr is not None
        and gravitational_constant is not None
        and m_2 is not None
        and distance is not None
    ):
        return force_gr * pow(distance, 2) / (gravitational_constant * pow(m_2, 2))
    # print("force_gr = gravitational_constant * (m_1 * m_2) / distance^2")
    # return gravitational_constant * (m_1 * m_2) / pow(distance, 2)
    if density is not None and volume is not None:
        print("mass = density * volume")
        return density * volume
    if amount_of_substance_in_moles is not None and molar_mass is not None:
        print("mass = amount of substance in moles * molar mass")
        return amount_of_substance_in_moles * molar_mass
    if mass_of_one_molecule is not None and number_of_particles is not None:
        print("mass = mass of one molecule/atom * number of particles")
        return mass_of_one_molecule * number_of_particles
    if weight_force is not None and acceleration_of_gravity is not None:
        print("mass = weight force / acceleration of gravity")
        return weight_force / acceleration_of_gravity
    if (
        total_energy_of_a_free_body is not None
        and speed_of_light is not None
        and impulse is not None
    ):
        print(
            "mass^2 = (total energy of a free body^2 / speed of light^4) - (impulse^2 / speed of light^2)"
        )
        return (pow(total_energy_of_a_free_body, 2) / pow(speed_of_light, 4)) - pow(
            impulse, 2
        ) / pow(speed_of_light, 2)


def weight_formula(mass, acceleration_of_gravity=9.81) -> float:
    # Основная фомула веса: масса умноженная на ускорение гравитации
    print("weight = mass * acceleration of gravity")
    return mass * acceleration_of_gravity


def speed_formula(distance, time) -> float:
    # Основная фомула скорости: пройденное расстояние делить на время движения
    print("speed = distance / time")
    return distance / time


def the_second_liberation_cosmic_velocity_of_the_body_formula(
    radius_of_the_planet: float,
    orbit_altitude: float,
    orbital_speed: float,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float,
    gravitational_constant: float,
) -> float:
    print(
        "math.sqrt((2 * gravitational_constant * the_mass_of_the_planet_in_terms_of_Earth_masses) / (radius_of_the_planet + orbit_altitude))"
    )
    return math.sqrt(
        (2 * gravitational_constant * the_mass_of_the_planet_in_terms_of_Earth_masses)
        / (radius_of_the_planet + orbit_altitude)
    )


# хз че это
def boyles_law_formula(gas_pressure: float, gas_volume: float) -> float:
    return gas_pressure * gas_volume  # constant_value_under_given_conditions


module_help = """
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
) -> float
    расчет веса:
    2. weight_formula(mass, acceleration_of_gravity=9.81) -> float
    расчет скорости:
    3. speed_formula(distance, time) -> float
    расчет второй (освобожденной) космической скорости тела:
    4. the_second_liberation_cosmic_velocity_of_the_body_formula(
    radius_of_the_planet: float,
    orbit_altitude: float,
    orbital_speed: float,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float,
    gravitational_constant: float,
) -> float
    расчет закона Бойля - Мариотта:
    5. boyles_law_formula(gas_pressure: float, gas_volume: float) -> float
"""

if __name__ == "__main__":
    print("Module physics_lib is running")
else:
    print(f"module is included: {__name__}")
