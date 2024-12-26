from pathlib import Path

path = Path('learning_python.txt')
text = path.read_text(encoding='utf-8')
print(text.replace('Python', 'C'))