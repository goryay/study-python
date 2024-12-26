from pathlib import Path
import json

def get_favorite_number(path):
    if path.exists():
        content = path.read_text(encoding='utf-8')
        numbers = json.loads(content)
        return numbers
    else:
        return None

def get_new_favorite_number(path):
    number = int(input('Enter your a favorite number: '))
    content = json.dumps(number)
    path.write_text(content)
    return number

def show_favorite_number(path):
    path = Path('fn.json')
    numbers = get_favorite_number(path)
    if numbers:
        print(f"Your favorite number is {numbers}.")
    else:
        numbers = get_new_favorite_number(path)
        print(f"Your favorite new number is {numbers}.")

show_favorite_number(Path('fn.json'))