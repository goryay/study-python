from pathlib import Path

while True:
    print(f"Enter 'q' to quit.")
    name = input("Enter your name: ")
    if name == "q":
        break
    print(f"Hello, {name}!")
    # return name

    path = Path("guest_book.txt")
    with path.open("a") as file:
        file.write(f"Hello, {name}!\n")