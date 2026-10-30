Python Multitool - инструмент предназначенный для решения математических, физических и других видов задач.

Правила написания кода:  
при написании кода в каждом модуле должен присутствовать этот паттерн в конце файла:

```python
if __name__ == "__main__":
    print(f"Module {Название модуля} is running")
else:
    print(f"module is included: {__name__}")

# Пример
if __name__ == "__main__":
    print("Module math_lib is running")
else:
    print(f"module is included: {__name__}")
```

Названием модуля является название файла.  
Это нужно для проверки подключенных модулей к запускаемому коду.

Что реализовано:
Классы в physics_lib предназначенные для преобразования величин в разные единицы измерения:  
    Time - время;  
    Distance - расстояние/длинна;  
    Mass - масса;  
    Pressure - давление;  
    Volume - объем;  
    DataStorage - объем информации (класс нужно перенести в другой модуль);  
    PlaneAngle - плоский угол;  
    Area - площадь;  
    FuelConsumption - расход топлива;  
    Speed - скорость;  
    DataTransferRate - скорость передачи данных;  
    Frequency - частота;  
    Energy - энергия;  
    Temperature - температура;  
функции в physics_lib:
    физические формулы:
    расчет массы:
    1. mass_formula(force=None, acceleration=None, m_1=None, m_2=None, distance=None, density=None, volume=None, amount_of_substance_in_moles=None, molar_mass=None, mass_of_one_molecule=None, number_of_particles=None, weight_force=None, total_energy_of_a_free_body=None, speed_of_light=None, impulse=None, force_gr=None, gravitational_constant=6.6743015 * pow(10, -11), acceleration_of_gravity=9.81,)  
    расчет веса:  
    2. weight_formula(mass, acceleration_of_gravity=9.81)  
    расчет скорости:  
    3. speed_formula(distance, time)  

Что нужно реализовать:
в physics_lib:  
    valence_of_chemical_elements;  
    the_second_liberation_cosmic_velocity_of_the_body_formula;  
    boyles_law_formula;  
    gay_lussacs_law_formula;  
    kinetic_energy_of_the_body_formula;  
    concentration_of_solutions_formula;  
    mass_of_a_substance_in_a_solution_formula;  
    moment_of_force_formula;  
    the_magnitude_of_the_mass_and_acceleration_of_bodies_according_to_Newtons_third_law_formula;  
    the_molar_mass_of_the_gas_formula;  
    normal_acceleration_when_moving_in_a_circle_formula;  
    determine_how_a_moving_body_accelerates_formula;  
    the_first_orbital_cosmic_velocity_of_a_body_formula;  
    potential_energy_formula;  
    height_formula;  
    tangential_acceleration_formula;  
    velocity_formula;  
    time_formula;  
    Radioactivity_formula;  
    half_life_formula;  
    power_formula;  
    force_formula;  
    acceleration_of_a_body_formula;  
    Newtons_second_law_formula;  
    Ohms_law_for_a_section_of_a_circuit_formula;  
    speed_of_sound_in_air_formula;  
    the_third_cosmic_velocity_of_a_body_formula; 
    distance_formula;  
    clapeyron_equation_formula;  
    ideal_gas_equation_formula;  
    centripetal_acceleration_when_moving_in_a_circle_formula;  

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
    8. quadratic_equation_formula(a, b, c)
