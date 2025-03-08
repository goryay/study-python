sandwich_orders = ['пастрама', 'с колбасой', 'c сыром', 'пастрама', 'с колбасой и сыром', 'с икрой и рыбой', 'с маслом', 'пастрама']
finished_sandwich = []

print(f"До удаление пастрамы из списка - {sandwich_orders}")
while 'пастрама' in sandwich_orders:
    sandwich_orders.remove('пастрама')
print(f"После удаления пастрамы из списка - {sandwich_orders}")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Я приготовил бутер {current_sandwich}")
    finished_sandwich.append(current_sandwich)

print(f"Приготовленны следующие бутерброды:")
for sandwich in finished_sandwich:
    print(sandwich)