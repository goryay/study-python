cities = {
    'Moscow': {
        'population': 15_000_000,
        'country': 'Russia',
        'facts': 'Lenin'
    },
    'Siant-Petesburg': {
        'population': 5_000_000,
        'country': 'Russia',
        'facts': '1703'
    },
    'Volgograd': {
        'population': 800_000,
        'country': 'Russia',
        'facts': 'Stalingrad'
    }
}

for name, information in cities.items():
    print(f"\nName: {name}")
    population = f"{information['population']} population"
    country = f"{information['country']} country"
    facts = f"{information['facts']} facts"
    print(f"Population: {population}")
    print(f"Country: {country}")
    print(f"Facts: {facts}")