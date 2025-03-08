def make_album(album_name, performer_name, number_of_songs=None):
    creator = {'album': album_name, 'performer': performer_name}
    if number_of_songs:
        creator['number_of_songs'] = number_of_songs
    return creator


# album_name = input("Enter album name: ")
# performer_name = input("Enter performer name: ")
# person = make_album(album_name, performer_name)
# print(person)

while True:
    print(f"Enter q to quit")
    a_name = input("Enter album name: ")
    if a_name == "q":
        break

    p_name = input("Enter performer name: ")
    if p_name == "q":
        break

    formatted_name = make_album(a_name, p_name)
    print(f"{formatted_name}")

print(make_album('Golden cobra', 'Limp Bizkit'))
print(make_album('Offline', 'Guano Apes', 16))
