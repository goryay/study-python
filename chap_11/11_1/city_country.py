from cities_countries_function import get_cities_countries

print(f"Entry 'q' to quit.")
while True:
    city_name = input(f'Enter city name: ')
    if city_name == 'q':
        break
    country_name = input(f'Enter country name: ')
    if country_name == 'q':
        break
    population = input(f'Enter population: ')
    if city_name == 'q':
        break

    population = population if population else None

    formatted_name = get_cities_countries(city_name, country_name, population)
    print(formatted_name)