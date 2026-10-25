import physics_lib


def something():
    print(
        "_______________________Проверка преобразований единиц измерения:_____________________"
    )
    fuel = physics_lib.FuelConsumption(1, "liter_per_100_km")
    print(fuel)
    fuel.convert("imperial_mpg")
    print(fuel)
    fuel2 = physics_lib.FuelConsumption(1, "imperial_mpg")
    print(fuel2)
    fuel2.convert("liter_per_100_km")
    print(fuel2)

    print("_______________________Проверка функции расчета массы_____________________")
    # Второй закон Ньютона: F = m * a => m = F / a
    force = 100.0
    acceleration = 2.0
    expected = 50.0
    result = physics_lib.mass_formula(force=force, acceleration=acceleration)
    print(f"Result: {result}, expected: {expected}")

    # Плотность: m = density * volume
    density = 2.5
    volume = 4.0
    expected = 10.0
    result = physics_lib.mass_formula(density=density, volume=volume)
    print(f"Result: {result}, expected: {expected}")

    # Количество вещества: m = n * M
    amount = 2.0
    molar_mass = 18.015  # например, вода
    expected = 36.03
    result = physics_lib.mass_formula(
        amount_of_substance_in_moles=amount, molar_mass=molar_mass
    )
    print(f"Result: {result}, expected: {expected}")

    # Масса через число частиц: m = m0 * N
    mass_of_one = 1.66e-27
    number_of_particles = 6.022e23
    expected = mass_of_one * number_of_particles
    result = physics_lib.mass_formula(
        mass_of_one_molecule=mass_of_one, number_of_particles=number_of_particles
    )
    print(f"Result: {result}, expected: {expected}")

    # Через вес тела: m = P / g
    body_weight = 98.1
    acceleration_of_gravity = 9.81
    expected = 10.0
    result = physics_lib.mass_formula(
        body_weight=body_weight, acceleration_of_gravity=acceleration_of_gravity
    )
    print(f"Result: {result}, expected: {expected}")

    # Релятивистская формула массы: m^2 = (E^2 / c^4) - (p^2 / c^2)
    total_energy = 3.0
    speed_of_light = 1.0
    impulse = 0.0
    # (3^2 / 1^4) - (0^2 / 1^2) = 9 - 0 = 9
    expected = 9.0
    result = physics_lib.mass_formula(
        total_enrgy_of_a_free_body=total_energy,
        speed_of_light=speed_of_light,
        impulse=impulse,
    )
    print(f"Result: {result}, expected: {expected}")

    print("_______________________Проверка функции расчета веса_____________________")

    # physics_lib._weight_formula(mass, acceleration_of_gravity=9.81)
    print("Mass = 10")
    print("Acceleration of gravity = 9.81")
    print(physics_lib.weight_formula(mass=10))

    print(
        "_______________________Проверка функции расчета скорости_____________________"
    )

    # _speed_formula(distance, time)
    print("Distance = 20")
    print("Time = 100")
    print(physics_lib.speed_formula(distance=20, time=100))


print("""
------------------------------------------------------------
tests///////////////////////////////////////////////////////
------------------------------------------------------------
""")

something()

print("""
------------------------------------------------------------
tests///////////////////////////////////////////////////////
------------------------------------------------------------
""")
