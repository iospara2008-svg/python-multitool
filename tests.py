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
    result = physics_lib.mass_formula(force=100, acceleration=2)
    print(f"Result: {result}, expected: 50")

    # Плотность: m = density * volume
    result = physics_lib.mass_formula(density=2.5, volume=4)
    print(f"Result: {result}, expected: 10")

    # Количество вещества: m = n * M
    result = physics_lib.mass_formula(amount_of_substance_in_moles=2, molar_mass=18.015)
    print(f"Result: {result}, expected: 36.03")

    # Масса через число частиц: m = m0 * N
    expected = 1.66e-27 * 6.022e23
    result = physics_lib.mass_formula(
        mass_of_one_molecule=1.66e-27, number_of_particles=6.022e23
    )
    print(f"Result: {result}, expected: {expected}")

    # Через вес тела: m = P / g
    result = physics_lib.mass_formula(weight_force=98.1, acceleration_of_gravity=9.81)
    print(f"Result: {result}, expected: 10")

    # Релятивистская формула массы: m^2 = (E^2 / c^4) - (p^2 / c^2)
    # (3^2 / 1^4) - (0^2 / 1^2) = 9 - 0 = 9
    result = physics_lib.mass_formula(
        total_energy_of_a_free_body=3,
        speed_of_light=1,
        impulse=0,
    )
    print(f"Result: {result}, expected: 9")

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
