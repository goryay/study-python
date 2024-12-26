from pathlib import Path

file = Path('pg.txt')
word = input('Enter a word: ')

while True:
    try:
        content = file.read_text(encoding='utf-8')
        count = content.lower().count(word)
    except FileNotFoundError:
        pass
        break
    else:
        print(f"The word '{word}' occurs {count} times in the file.")
        break
