# person = {'age': 26, 'first_name': 'Илья', 'last_name': 'Горяйнов','city': 'Москва'}
#
# print(f"Имя: {person['first_name']}")
# print(f"Фамилия: {person['last_name']}")
# print(f"Возраст: {person['age']}")
# print(f"Город: {person['city']}")

peopls = {
    'pasha':{'first':'pavel','last':'durov','city':'dubai'},
    'sasha':{'first':'alex','last':'ushakov','city':'moscow'}
}

for username,user_info in peopls.items():
    print('\nUsername: ' + username.title())
    full_name = user_info['first'] + ' ' + user_info['last']
    city = user_info['city']
    print('Full name: '+full_name.title())
    print('City: '+ city.title())