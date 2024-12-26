import random

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

winning_combo = random.sample(elements, 4)

print(f"The winning ticket is: {winning_combo}")
print("Congratulations! Your ticket with this combination is the winner!")
