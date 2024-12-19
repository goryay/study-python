pets = {
    'gera': {
        'парода': 'бурма',
        'возраст': '1 год',
        'пол': 'ж',

},
    'barri': {
        'парода': 'французский бульдог',
        'возраст': '10 лет',
        'пол': 'м',
    }
}

for pet, pet_info in pets.items():
    print(f"Nickname: {pet.title()}")
    paroda = pet_info['парода']
    print(f"Paroda: {paroda}")
    age = pet_info['возраст']
    print(f"Age: {age}")
    sex = pet_info['пол']
    print(f"Sex: {sex}")