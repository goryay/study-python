guest_list = ['leonid', 'ivan', 'roma', 'max', 'kirill']
print(guest_list)

print(f"{guest_list[0].title()}, you're invited to a party.")
print(f"{guest_list[1].title()}, you're invited to a party.")
print(f"{guest_list[2].title()}, you're invited to a party.")
print(f"{guest_list[3].title()}, you're invited to a party.")
print(f"{guest_list[4].title()}, you're invited to a party.")

print('----------------------------------------------------')

removed_guest = 'ivan'
guest_list.remove(removed_guest)
print(guest_list)
print(f'removed guest: {removed_guest.title()}')

new_guest = 'ilya'
guest_list.insert(1, new_guest)
print(guest_list)

print(f"{guest_list[1].title()}, you're invited to a party.")

print('----------------------------------------------------')

print(f"I've got a new bit table!")
more_guest_list = 'Lena'
second_guest_list = 'Bob'
last_guest_list = 'Lilya'
guest_list.insert(0, more_guest_list)
guest_list.insert(3, second_guest_list)
guest_list.append(last_guest_list)
print(f'Guest list: {guest_list}')

print('----------------------------------------------------')

print(f"I'm sorry, I can invited 2 guest only")
not_invited = guest_list.pop(-1)
print(f"{not_invited}, sorry")
print(guest_list)
not_invited = guest_list.pop(-1)
print(f"{not_invited}, sorry")
print(guest_list)
not_invited = guest_list.pop(-1)
print(f"{not_invited}, sorry")
print(guest_list)
not_invited = guest_list.pop(-1)
print(f"{not_invited}, sorry")
print(guest_list)
not_invited = guest_list.pop(-1)
print(f"{not_invited}, sorry")
print(guest_list)
not_invited = guest_list.pop(-1)
print(f"{not_invited}, sorry")
print(guest_list)
print(f"{guest_list[0]}, you're invited to a party.")
print(f"{guest_list[1]}, you're invited to a party.")
del guest_list[1]
print(guest_list)
del guest_list[0]
print(guest_list)