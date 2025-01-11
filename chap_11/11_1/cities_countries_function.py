def get_cities_countries(city_name, country_name, population=''):
    if population:
        cities_countries = f"{city_name} {country_name} {population}"
    else:
        cities_countries = f"{city_name} {country_name}"
    return cities_countries.title()