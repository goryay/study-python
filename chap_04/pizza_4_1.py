pizzas = ['margherita', 'hawaii', 'napoli', 'pepperoni', 'cheese', 'four season', 'vegetables']
friend_pizzas = pizzas[:]
for pizza in pizzas:
    print('I love ' + pizza.title())


print("I love pizza so much!\n")

print(f'The first three items on the list are {pizzas[:3]}')
print(f'Three points out of the middle are {pizzas[2:5]}')
print(f'The last three items on the list are {pizzas[-3:]}')

pizzas.append('marinara')
friend_pizzas.append('pomodoro')

print(f'My list: {pizzas}')
print(f'My friend list: {friend_pizzas}')
