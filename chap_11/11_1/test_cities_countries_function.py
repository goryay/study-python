from cities_countries_function import get_cities_countries

def test_cities_countries_name():
    formated_name = get_cities_countries('santiago', 'chile')
    assert formated_name == 'Santiago Chile'


def test_cities_countries_population():
    formated_name = get_cities_countries('santiago', 'chile', 5_000_000)
    assert formated_name == 'Santiago Chile 5000000'