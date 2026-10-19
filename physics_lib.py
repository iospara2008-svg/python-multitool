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


# создание объекта: object_mass = _Mass(value, "kilogram")
class _Mass:
    # Создание объекта (экземлпяра класса), инициализация принимает аргументы: Количество что является произвольной величиной
    # не зависящей от единицы измерения и название единицы измерения для ее определения
    def __init__(self, _value: float, _dimension: str):
        _dimension = _dimension.lower()

        if hasattr(self, _dimension):  # если класс имеет арибут совпадающий с
            setattr(self, _dimension, True)  # названием переданного аргумента
            # то атрибуту присваивается значение True.

            # преобразование value в соответствии с переданным аргументом _dimension.
            self.value = _value
            self.dimension = _dimension

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

    # Основные единицы измерения
    microgram: bool = False
    milligram: bool = False
    gram: bool = False
    kilogram: bool = False
    centner: bool = False
    ton: bool = False

    # Допольнительны единицы измерения
    pound: bool = False
    ounce: bool = False
    carat: bool = False

    # Словарь для преобразования имзерений относительно грамма
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


# Mass Inertial and Gravitational
# Масса - скалярная величина, определяющая инертные и гравитационные свойства тел.
# Масса эквивалентна энергии покоя
def _mass_formula(
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
    body_weight=None,
    total_enrgy_of_a_free_body=None,
    speed_of_light=None,
    impulse=None,
    gravitational_constant=6.6743015 * pow(10, -11),
    acceleration_of_gravity=9.81,
):  # Inertial mass
    if force is not None and acceleration is not None:
        print("force = mass * acceleration -> mass = force / acceleration")
        return force / acceleration
    # print("force_gr = gravitational_constant * (m_1 * m_2) / distance^2")
    # return gravitational_constant * (m_1 * m_2) / pow(distance, 2)
    elif density is not None and volume is not None:
        print("mass = density * volume")
        return density * volume
    elif amount_of_substance_in_moles is not None and molar_mass is not None:
        print("mass = amount of substance in moles * molar mass")
        return amount_of_substance_in_moles * molar_mass
    elif mass_of_one_molecule is not None and number_of_particles is not None:
        print("mass = mass of one molecule/atom * number of particles")
        return mass_of_one_molecule * number_of_particles
    elif body_weight is not None and acceleration_of_gravity is not None:
        print("mass = body weight / acceleration of gravity")
        return body_weight / acceleration_of_gravity
    elif (
        total_enrgy_of_a_free_body is not None
        and speed_of_light is not None
        and impulse is not None
    ):
        print(
            "mass^2 = (total energy of a free body^2 / speed of light^4) - (impulse^2 / speed of light^2)"
        )
        return (pow(total_enrgy_of_a_free_body, 2) / pow(speed_of_light, 4)) - pow(
            impulse, 2
        ) / pow(speed_of_light, 2)


def _weight_formula(mass, acceleration_of_gravity=9.81):
    return mass * acceleration_of_gravity


if __name__ == "__main__":
    print("Module physics_lib is running")
else:
    print(f"module is included: {__name__}")
