# users = []
users = ['admin', 'user', 'moderator', 'man', 'woman']

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin! Do you want to look a report?')
        else:
            print('Hello! Thank you for logging in again.')
else:
    print('No users found!')