alien_color = ['green', 'yellow', 'red']
# if 'green' in alien_color:
#     print(f'You have 5 points.')

# if 'black' in alien_color:
#     print(f'You don\'t have 5 points.')

# else:
#     print('You have 10 points.')

if 'green' in alien_color:
    print(f"You have earned 5 points.")
elif 'yellow' in alien_color:
    print(f"You have earned 10 points.")
elif 'red' in alien_color:
    print(f"You have earned 15 points.")
else:
    print(f"Sorry, you do not have enough alien points.")