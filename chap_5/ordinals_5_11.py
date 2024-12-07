ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in ordinal_numbers:
    if number == 1:
        print(f'{number}st')
    if number == 2:
        print(f'{number}nd')
    if number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
