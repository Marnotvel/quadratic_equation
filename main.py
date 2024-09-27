import math

print("Квадратное уравнение имеет вид ax^2 + bx + c = 0")
print("Введите коэффициенты уравнения, которое хотите решить")

first_number = float(input("Введите число 'a' "))
second_number = float(input("Введите число 'b' "))
third_number = float(input("Введите число 'c' "))

if first_number == 0:
    if second_number == 0:
        if third_number == 0:
            print("x любое")
        else:
            print("Нет решения")

    else:
        print(f"Корень {format(-third_number/second_number, '.2f')}")
else:
    discr = second_number ** 2 - 4 * first_number * third_number

    if discr > 0:

        x1 = format((-second_number + math.sqrt(discr)) / (2 * first_number), '.2f')
        x2 = format((-second_number - math.sqrt(discr)) / (2 * first_number), '.2f')
        print(f"Найденные корни: {x1} и {x2}")

    elif discr == 0:

        x = format(-second_number / (2 * first_number), '.2f')
        print(f"Найденный корень: {x}")

    else:
        discr = (math.sqrt(-discr))
        first_part = format(second_number / 2 * first_number, '.2f')
        second_part = format(discr / 2 * first_number, '.2f')

        print(f"Найденные корни: {first_part} + {second_part}i и {first_part} - {second_part}i")