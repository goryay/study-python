current_users = ['Goryay', 'Skufo', 'somirage', 'oIvan', 'sky']
new_users = ['mag', 'cowboy', 'Skufo', 'ezra', 'oIvan']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'This username is "{new_user}" used.')
    else:
        print(f'You can use this username "{new_user}".')