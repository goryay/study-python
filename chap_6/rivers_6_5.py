rivers = {
    'nile': 'egypt',
    'volga': 'russia',
    'dnepr': 'ukraine',
    'amazonka': 'brazil',
}

for river, country in rivers.items():
    print(f"The {river.title()} is in {country.title()}")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)