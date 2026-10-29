# math

# constants & variables #
Pi = 3.1415926535
Imaginary_unit = 0 + 1j  # or 0 + 1i; complex(0, 1)
Eulers_number = 2.7182818284
Square_root_of_2 = Pythagoras_constant = 1.4142135623  # or math.sqrt(2)
Square_root_of_3 = Theodorus_constant = 1.7320508075  # or math.sqrt(3)
Golden_ratio = 1.6180339887
Cube_root_of_2 = 1.2599210498  # or 2 ** (1/3); math.cbrt(2); pow(1/3, 2)
Natural_logarithm_of_2 = 0.6931471805  # or math.log(2)
Euler_Mascheroni_constant = 0.5772156649
Aperys_constant = 1.2020569031
Catalans_constant = 0.9159655941
Lemniscate_constant = 2.6220575542
Glaisher_Kinkelin_constant = 1.2824271291
Khinchins_constant = 2.6854520010
Feigenbaum_constant_1 = 4.6692016091
Feigenbaum_constant_2 = 2.5029078750


# Formulas for abbreviated multiplication #
def square_of_the_sum_formula(a: float, b: float):  # Square of the sum
    print("(a + b)^2 = a^2 + 2ab + b^2")
    return pow((a + b), 2)


def square_of_the_difference_formula(a: float, b: float):  # Square of the difference
    print("(a - b)^2 = a^2 - 2ab + b^2")
    return pow((a - b), 2)


def difference_of_squares_formula(a: float, b: float):  # Difference of squares
    print("a^2 - b^2 = (a - b)(a + b)")
    return pow(a, 2) - pow(b, 2)


def difference_of_cubes_formula(a: float, b: float):  # Difference of cubes
    print("a^3 - b^3 = (a - b)(a^2 + ab + b^2)")
    return pow(a, 3) - pow(b, 3)


def sum_of_cubes_formula(a: float, b: float):  # Sum of cubes
    print("a^3 + b^3 = (a + b)(a^2 - ab + b^2)")
    return pow(a, 3) + pow(b, 3)


def cube_of_sum_formula(a: float, b: float):  # Cube of sum
    print("(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3")
    return pow((a + b), 3)


def difference_of_cube_formula(a: float, b: float):  # Difference of cube
    print("(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3")
    return pow((a - b), 3)


# Quadratic equation formula
def quadratic_equation_formula(a: float, b: float, c: float):
    print("Let the quadratic equation have the form: ax^2 + bx + c = 0")
    x1 = 0
    x2 = 0
    if a == 0 and b == 0 and c == 0:
        return "infinite_solutions"
    elif a == 0 and b != 0 and c != 0:
        x1 = -(c / b)
        return x1
    elif a == 0 and b == 0 and c != 0:
        return "no_solution"
    elif a == 0 and b != 0 and c == 0:
        x1 = 0
        return x1
    else:
        disc = (b**2) - (4 * a * c)  # discriminant
        if disc == 0:
            x1 = (-b) / (2 * a)
            return x1
        elif disc > 0:
            x1 = (-b - (disc**0.5)) / (2 * a)
            x2 = (-b + (disc**0.5)) / (2 * a)
            return (min(x1, x2), max(x1, x2))
        elif disc < 0:
            return "no_solution"


module_help = """
Модуль math_lib содержит следующие функции:
    формулы сокращенного умножения:
    1. square_of_the_sum_formula(a, b)
    2. square_of_the_difference_formula(a, b)
    3. difference_of_squares_formula(a, b)
    4. difference_of_cubes_formula(a, b)
    5. sum_of_cubes_formula(a, b)
    6. cube_of_sum_formula(a, b)
    7. difference_of_cube_formula(a, b)
    формула квадратного уравнения:
    8. quadratic_equation(a, b, c)
"""

if __name__ == "__main__":
    print("Module math_lib is running")
    print(module_help)
else:
    print(f"module is included: {__name__}")
