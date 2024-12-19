favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phill': 'python'}
polls = ['jen', 'sarah', 'edward', 'phill', 'nik', 'david', 'valera']

for name in polls:
    if name in favorite_languages:
        print(f"{name.title()} thanks for tacking the poll!")
    else:
        print(f"{name.title()}, please take the poll!")