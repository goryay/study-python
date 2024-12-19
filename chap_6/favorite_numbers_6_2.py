favorite_numbers = {
    'Ilya': {'69', '96'},
    'Kirill': '25',
    'Roma': '1',
    'Leonid': '40',
    'Ivan': {'100', '999'},
}

# print(f"Любимое число Ильи - {favorite_numbers['Ilya']}")
# print(f"Любимое число Кирилла - {favorite_numbers['Kirill']}")
# print(f"Любимое число Ромы - {favorite_numbers['Roma']}")
# print(f"Любимое число Леонида - {favorite_numbers['Leonid']}")
# print(f"Любимое число Ивана - {favorite_numbers['Ivan']}")

for key, values in favorite_numbers.items():
    print(f"Любимое число {key.title()}")
    for value in values:
        print(value)