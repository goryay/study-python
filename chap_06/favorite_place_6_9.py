favorite_place = {
    'msc': {
        'name': 'moscow',
        'country': 'russia',
        'populate place': 'red square'
    },
    'uk': {
        'name': 'london',
        'country': 'united kingdom',
        'populate place': 'big ban'
    },
    'ny': {
        'name': 'new york',
        'country': 'usa',
        'populate place': 'time square'
    }
}

for nickname, places in favorite_place.items():
    print(f"Сокращенное название: {nickname}")
    city_name = f'place name: {places["name"].title()}'
    print(city_name)
    country = f'Country is {places["country"].title()}'
    print(country)
    populate_place = f'Populate place is {places["populate place"].title()}'
    print(populate_place)