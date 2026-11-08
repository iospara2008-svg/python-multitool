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


def check(*args):
    for arg in args:
        if arg is None:
            return False
    return True


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
    results: list = []

    if check(force, acceleration):
        print("force = mass * acceleration -> mass = force / acceleration")
        results.append(force / acceleration)
    if check(force_gr, gravitational_constant, m_2, distance):
        results.append(force_gr * pow(distance, 2) / (gravitational_constant * m_2))
    # print("force_gr = gravitational_constant * (m_1 * m_2) / distance^2")
    # return gravitational_constant * (m_1 * m_2) / pow(distance, 2)
    if check(density, volume):
        print("mass = density * volume")
        results.append(density * volume)
    if check(amount_of_substance_in_moles, molar_mass):
        print("mass = amount of substance in moles * molar mass")
        results.append(amount_of_substance_in_moles * molar_mass)
    if check(mass_of_one_molecule, number_of_particles):
        print("mass = mass of one molecule/atom * number of particles")
        results.append(mass_of_one_molecule * number_of_particles)
    if check(weight_force, acceleration_of_gravity):
        print("mass = weight force / acceleration of gravity")
        results.append(weight_force / acceleration_of_gravity)
    if check(total_energy_of_a_free_body, speed_of_light, impulse):
        print(
            "mass^2 = (total energy of a free body^2 / speed of light^4) - (impulse^2 / speed of light^2)"
        )
        results.append(
            (pow(total_energy_of_a_free_body, 2) / pow(speed_of_light, 4))
            - pow(impulse, 2) / pow(speed_of_light, 2)
        )

    return results


def weight_formula(
    mass: float = None,
    acceleration_of_gravity: float = 9.81,
) -> float:
    results: list = []

    # Основная фомула веса: масса умноженная на ускорение гравитации
    if check(mass, acceleration_of_gravity):
        print("weight = mass * acceleration of gravity")
        results.append(mass * acceleration_of_gravity)

    return results


def speed_formula(
    distance: float = None,
    time: float = None,
) -> float:
    results: list = []

    # Основная фомула скорости: пройденное расстояние делить на время движения
    if check(distance, time):
        print("speed = distance / time")
        results.append(distance / time)

    return results


def the_second_liberation_cosmic_velocity_of_the_body_formula(
    radius_of_the_planet: float = None,
    orbit_altitude: float = None,
    orbital_speed: float = None,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float = None,
    gravitational_constant: float = 6.6743015 * pow(10, -11),
) -> float:
    results: list = []

    if check(
        radius_of_the_planet,
        orbit_altitude,
        orbital_speed,
        the_mass_of_the_planet_in_terms_of_Earth_masses,
        gravitational_constant,
    ):
        print(
            "math.sqrt((2 * gravitational_constant * the_mass_of_the_planet_in_terms_of_Earth_masses) / (radius_of_the_planet + orbit_altitude))"
        )
        results.append(
            math.sqrt(
                (
                    2
                    * gravitational_constant
                    * the_mass_of_the_planet_in_terms_of_Earth_masses
                )
                / (radius_of_the_planet + orbit_altitude)
            )
        )

    return results


def boyles_law_formula(
    gas_pressure: float = None,
    gas_volume: float = None,
) -> float:
    results: list = []

    if check(gas_pressure, gas_volume):
        results.append(
            gas_pressure * gas_volume
        )  # constant_value_under_given_conditions

    return results


def volumes_law_formula(
    gas_volume: float = None,
    temperature: float = None,
) -> float:
    results: list = []

    if check(gas_volume, temperature):
        results.append(gas_volume / temperature)  # const

    return results


def gay_lussacs_second_law_formula(
    gas_pressure: float = None,
    temperature: float = None,
) -> float:
    results: list = []

    if check(gas_pressure, temperature):
        results.append(gas_pressure / temperature)  # gas_pressure

    return results


def kinetic_energy_of_the_body_formula(
    mass: float = None,
    speed: float = None,
) -> float:
    results: list = []

    if check(mass, speed):
        results.append(mass * pow(speed, 2) / 2)

    return results


def mixture_concentration_formula(
    component_mass: float = None,
    total_mass_of_all_components_of_the_mixture: float = None,
) -> float:
    results: list = []

    if check(component_mass, total_mass_of_all_components_of_the_mixture):
        results.append(component_mass / total_mass_of_all_components_of_the_mixture)

    return results


def moment_of_force_formula(
    force_module: float = None,
    shoulder_strength: float = None,
) -> float:
    results: list = []

    if check(force_module, shoulder_strength):
        results.append(force_module * shoulder_strength)

    return results


def newtons_third_law_formula(
    force_1: float = None,
) -> float:
    results: list = []

    if check(force_1):
        results.append(-force_1)  # force_2

    return results


def molar_mass_of_gas_formula(
    mass_of_gas: float = None,
    amount_of_substance_in_moles: float = None,
    gas_density: float = None,
    density: float = None,
    universal_gas_constant: float = None,
    temperature_in_kelvin: float = None,
    pressure: float = None,
    molar_volume: float = 22.4,
) -> float:
    results: list = []

    if check(mass_of_gas, amount_of_substance_in_moles):
        results.append(mass_of_gas / amount_of_substance_in_moles)
    if check(gas_density, molar_volume):
        results.append(gas_density * molar_volume)  # Through molar volume
    if check(density, universal_gas_constant, temperature_in_kelvin, pressure):
        results.append(
            density * universal_gas_constant * temperature_in_kelvin
        ) / pressure  # From the Mendeleev-Clapeyron equation

    return results


def normal_acceleration_when_moving_in_a_circle_formula(
    radius: float = None,
    speed: float = None,
    angular_velocity: float = None,
) -> float:
    results: list = []

    if check(speed, radius):
        results.append(pow(speed, 2) / radius)
    if check(angular_velocity, radius):
        results.append(pow(angular_velocity, 2) * radius)

    return results


def acceleration_formula(
    initial_speed: float = None,
    final_speed: float = None,
    time: float = None,
    force: float = None,
    mass: float = None,
) -> float:
    results: list = []

    if check(final_speed, initial_speed, time):
        results.append((final_speed - initial_speed) / time)
    if check(force, mass):
        results.append(force / mass)

    return results


def the_first_orbital_cosmic_velocity_of_a_body_formula(
    radius_of_the_planet: float = None,
    orbit_altitude: float = None,
    orbital_speed: float = None,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float = None,
    gravitational_constant: float = 6.6743015 * pow(10, -11),
) -> float:
    results: list = []

    if check(
        radius_of_the_planet,
        orbit_altitude,
        orbital_speed,
        the_mass_of_the_planet_in_terms_of_Earth_masses,
        gravitational_constant,
    ):
        results.append(
            math.sqrt(
                (
                    gravitational_constant
                    * the_mass_of_the_planet_in_terms_of_Earth_masses
                )
                / (radius_of_the_planet + orbit_altitude)
            )
        )

    return results


def centrifugal_force_formula(
    mass: float = None,
    speed: float = None,
    radius: float = None,
    angular_velocity: float = None,
) -> float:
    results: list = []

    if check(mass, speed, radius):
        results.append((mass * pow(speed, 2)) / radius)
    if check(mass, angular_velocity, radius):
        results.append(mass * pow(angular_velocity, 2) * radius)

    return results


def potential_energy_formula(
    mass: float = None,
    acceleration_of_gravity: float = None,
    height: float = None,
    body_stiffness_coefficient: float = None,
    absolute_deformation: float = None,
) -> float:
    results: list = []

    if check(mass, acceleration_of_gravity, height):
        results.append(mass * acceleration_of_gravity * height)
    if check(body_stiffness_coefficient, absolute_deformation):
        results.append((body_stiffness_coefficient * pow(absolute_deformation, 2)) / 2)

    return results


def tangential_acceleration_formula(
    final_speed: float = None,
    initial_speed: float = None,
    delta_time: float = None,
) -> float:
    results: list = []

    if check(final_speed, initial_speed, delta_time):
        results.append((final_speed - initial_speed) / delta_time)

    return results


def mass_of_matter_over_time_formula(
    initial_number_of_cores: float = None,
    half_life: float = None,
) -> float:
    results: list = []

    if check(initial_number_of_cores, half_life):
        results.append(initial_number_of_cores * pow(2, -(1 / half_life)))

    return results


def mechanic_power_formula(
    work: float = None,
    time: float = None,
    force: float = None,
    speed: float = None,
    torque: float = None,
    angular_velocity: float = None,
) -> float:
    results: list = []

    if check(work, time):
        results.append(work / time)
    if check(force, speed):
        results.append(force * speed)
    if check(torque, angular_velocity):
        results.append(torque * angular_velocity)

    return results


def direct_current_formula(
    voltage: float = None,
    amperage: float = None,
    resist: float = None,
) -> float:
    results: list = []

    if check(voltage, amperage):
        results.append(voltage * amperage)
    if check(amperage, resist):
        results.append(pow(amperage, 2) * resist)
    if check(voltage, resist):
        results.append(pow(voltage, 2) / resist)

    return results


def alternating_current_formula(
    voltage: float = None,
    amperage: float = None,
    active_power: float = None,
    reactive_power: float = None,
) -> float:
    results: list = []

    if check(voltage, amperage):
        results.append(voltage * amperage)
    if check(active_power, reactive_power):
        results.append(math.sqrt(pow(active_power, 2) + pow(reactive_power, 2)))

    return results


def force_formula(
    mass: float = None,
    acceleration: float = None,
) -> float:
    results: list = []

    if check(mass, acceleration):
        results.append(mass * acceleration)

    return results


def amperage_formula(
    charge: float = None,
    time: float = None,
    voltage: float = None,
    resist: float = None,
    electrical_power: float = None,
) -> float:
    results: list = []

    if check(charge, time):
        results.append(charge / time)
    if check(voltage, resist):
        results.append(voltage / resist)
    if check(electrical_power, voltage):
        results.append(electrical_power / voltage)

    return results


def speed_of_sound_formula(
    adiabatic_compressibility_of_the_medium: float = None,
    medium_density: float = None,
    adiabatic_index: float = None,
    universal_gas_constant: float = None,
    absolute_temperature_in_kelvin: float = None,
    molar_mass_of_gas: float = None,
    wavelength: float = None,
    oscillation_frequency: float = None,
    air_temperature_in_Celsius: float = None,
) -> float:
    results: list = []

    if check(adiabatic_compressibility_of_the_medium, medium_density):
        results.append(
            math.sqrt(1 / adiabatic_compressibility_of_the_medium * medium_density)
        )
    if check(
        adiabatic_index,
        universal_gas_constant,
        absolute_temperature_in_kelvin,
        molar_mass_of_gas,
    ):
        results.append(
            math.sqrt(
                (
                    adiabatic_index
                    * universal_gas_constant
                    * absolute_temperature_in_kelvin
                )
                / molar_mass_of_gas
            )
        )
    if check(wavelength, oscillation_frequency):
        results.append(wavelength * oscillation_frequency)
    if check(air_temperature_in_Celsius):
        results.append(331 + 0.6 * air_temperature_in_Celsius)

    return results


def the_third_cosmic_velocity_of_a_body_formula(
    orbital_speed_of_the_planet: float = None,
    the_planets_second_cosmic_velocity: float = None,
) -> float:
    results: list = []

    if check(orbital_speed_of_the_planet, the_planets_second_cosmic_velocity):
        results.append(
            math.sqrt(
                pow((math.sqrt(2) - 1), 2) * pow(orbital_speed_of_the_planet, 2)
                + pow(the_planets_second_cosmic_velocity, 2)
            )
        )

    return results


def ideal_gas_formula(
    gas_pressure: float = None,
    gas_volume: float = None,
    absolute_temperature_in_kelvin: float = None,
) -> float:
    results: list = []

    if check(gas_pressure, gas_volume, absolute_temperature_in_kelvin):
        results.append((gas_pressure * gas_volume) / absolute_temperature_in_kelvin)

    return results


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
    расчет закона Гей-Люссака:
    6. volumes_law_formula(gas_volume: float, temperature: float) -> float
    расчет второго закона Гей-Люссака:
    7. gay_lussacs_second_law_formula(gas_pressure, temperature: float) -> float
    расчет кинетической энергии тела:
    8. kinetic_energy_of_the_body_formula(mass: float, speed: float) -> float
    расчет концентрации растворов:
    9. mixture_concentration_formula(
    component_mass: float, total_mass_of_all_components_of_the_mixture: float
    ) -> float
    расчет момента силы:
    10. moment_of_force_formula(force_module: float, shoulder_strength: float) -> float
    расчет третьего закона Ньютона:
    11. newtons_third_law_formula(force_1: float) -> float
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
    ) -> float
    расчет нормального ускорения при движении по окружности:
    13. normal_acceleration_when_moving_in_a_circle_formula(
    radius: float,
    speed: float,
    angular_velocity: float,
    ) -> float
    расчет ускорения:
    14. acceleration_formula(
    initial_speed: float,
    final_speed: float,
    time: float,
    force: float,
    mass: float,
    ) -> float
    return (final_speed - initial_speed) / time
    расчет первой (орбитальной) космической скорости тела:
    15. the_first_orbital_cosmic_velocity_of_a_body_formula(
    radius_of_the_planet: float,
    orbit_altitude: float,
    orbital_speed: float,
    the_mass_of_the_planet_in_terms_of_Earth_masses: float,
    gravitational_constant: float,
    ) -> float
    расчет центробежной силы:
    16. centrifugal_force_formula(
    mass: float,
    speed: float,
    radius: float,
    angular_velocity: float,
    ) -> float
    расчет потенциальной энергии:
    17. potential_energy_formula(
    mass: float,
    acceleration_of_gravity: float,
    height: float,
    body_stiffness_coefficient: float,
    absolute_deformation: float,
    ) -> float
    расчет тангенциального ускорения:
    18. tangential_acceleration_formula(
    final_speed: float,
    initial_speed: float,
    delta_time: float,
    ) -> float
    расчет радиоактивного распада массы вещества через прошедшее время:
    19. mass_of_matter_over_time_formula(
    initial_number_of_cores: float,
    half_life: float,
    ) -> float
    расчет механической мощности:
    20. mechanic_power_formula(
    work: float,
    time: float,
    force: float,
    speed: float,
    torque: float,
    angular_velocity: float,
    ) -> float
    расчет постоянного тока:
    21. direct_current_formula(voltage: float, amperage: float, resist: float) -> float
    расчет переменного тока:
    22. alternating_current_formula(
    voltage: float,
    amperage: float,
    active_power: float,
    reactive_power: float,
    ) -> float
    расчет силы:
    23. force_formula(mass: float, acceleration: float) -> float
    расчет силы тока:
    24. amperage_formula(
    charge: float,
    time: float,
    voltage: float,
    resist: float,
    electrical_power: float,
    ) -> float
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
    ) -> float
    расчет третьей космической скорости тела:
    26. the_third_cosmic_velocity_of_a_body_formula(
    orbital_speed_of_the_planet: float,
    the_planets_second_cosmic_velocity: float,
    ) -> float
    расчет идеального газа:
    27. ideal_gas_formula(
    gas_pressure: float,
    gas_volume: float,
    absolute_temperature_in_kelvin: float,
    ) -> float
"""

if __name__ == "__main__":
    print("Module physics_lib is running")
    print(module_help)
else:
    print(f"module is included: {__name__}")
