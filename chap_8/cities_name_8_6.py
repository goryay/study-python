def city_country(name, country):
    return f"{name.title()}, {country.title()}"

name = input("Enter city name: ")
country = input("Enter country name: ")
b = city_country(name, country)
print(b)