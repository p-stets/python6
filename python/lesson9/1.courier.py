import math

# 60 5 3 / 4/5
# 40 2 10 / 2/2

'''
Задача 1. Курьер

Вам известен номер квартиры, этажность дома и количество квартир на этаже.
Задача: написать функцию, которая по заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.
'''

flat_nr = int(input("Flat number is: "))
floors_total = int(input("Input total floors: "))
flats_per_floar_count = int(input("Flats per floor is: "))


def calculate(flat_nr, floors_total, flats_per_floar_count):
    entrance_total = floors_total * flats_per_floar_count
    if flat_nr > entrance_total:
        entrance = flat_nr // entrance_total + 1
    else:
        entrance = 1
    if entrance == 1:
        floor = math.ceil((flat_nr / flats_per_floar_count))
    else:
        floor = math.ceil((flat_nr - (entrance - 1) * entrance_total) / flats_per_floar_count + 1)
    print(f'You need, the "{entrance}" entrance, the "{floor}" floor')


calculate(flat_nr, floors_total, flats_per_floar_count)


'''
def finish(flat_number, floors, max_flat_amount):
    import math
    max_flats = floors * max_flat_amount
    if flat_number > max_flats:
        entrace = math.ceil(flat_number / max_flats)
        print(entrace)
    else:
        entrace = 1
    if flat_number <= max_flats:
        needed_floor = math.ceil(flat_number / max_flat_amount)
    else:
        needed_floor = math.ceil((flat_number - (max_flats * (entrace - 1))) / max_flat_amount)
    return [entrace, needed_floor]

print(finish(40, 2, 10))
'''
