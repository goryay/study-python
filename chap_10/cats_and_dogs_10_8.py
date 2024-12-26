from pathlib import Path

def file_read(path):
    try:
        contents= path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File {path} not found.")
    else:
        print(contents)

files = ['cats.txt', 'dogs.txt', 'name.txt']
for file in files:
    path = Path(file)
    print(path)
    file_read(path)
