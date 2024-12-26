from pathlib import Path
import json


def get_sorted_username(path):
    if path.exists():
        contents = path.read_text()
        try:
            data = json.loads(contents)
            return data
        except json.JSONDecodeError:
            print("The file contains invalid JSON. Starting fresh.")
            return None
    else:
        return None


def get_new_username(path):
    username = input('Please enter your username: ')
    age = int(input('Please enter your age: '))
    city = input('Please enter your city: ')
    contents = json.dumps([username, age, city])
    path.write_text(contents)
    return [username, age, city]


def greet_user():
    path = Path('username.json')
    data = get_sorted_username(path)

    if data:
        username, age, city = data
        print(f"Is your username correct? (yes/no) {username}?")

        while True:
            answer = input().lower()
            if answer == 'yes':
                print(f'Welcome back, {username}!')
                print(f'Your age: {age}')
                print(f'From: {city}')
                break
            elif answer == 'no':
                data = get_new_username(path)
                username, age, city = data
                print(f"We'll remember you when you come back, {username}!")
                break
            else:
                print("Please answer with 'yes' or 'no'.")
    else:
        data = get_new_username(path)
        username, age, city = data
        print(f"We'll remember you when you come back, {username}!")


greet_user()
