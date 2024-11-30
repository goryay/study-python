countries = ["Россия", "США", "Китай", "Индия", "Япония"]

print("Исходный список:", countries)

print("Первая страна:", countries[0])
print("Последняя страна:", countries[-1])

countries[1] = "Канада"
print("После изменения второго элемента:", countries)

countries.append("Германия")
print("После добавления элемента в конец:", countries)

countries.insert(2, "Франция")
print("После вставки элемента на позицию 2:", countries)

del countries[3]
print("После удаления элемента с индексом 3:", countries)

countries.remove("Япония")
print("После удаления 'Япония':", countries)

last_country = countries.pop()
print("После извлечения последнего элемента:", countries)
print("Извлеченная страна:", last_country)

specific_country = countries.pop(1)
print("После извлечения элемента с индексом 1:", countries)
print("Извлеченная страна:", specific_country)

countries.sort()
print("После сортировки:", countries)

countries.sort(reverse=True)
print("После обратной сортировки:", countries)

print("Временная сортировка:", sorted(countries))
print("Список после временной сортировки:", countries)

countries.reverse()
print("После изменения порядка на обратный:", countries)

print("Длина списка:", len(countries))

print("Список стран:")
for country in countries:
    print(country)