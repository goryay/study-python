from administrator_9_7 import User, Admin

user = User('Kirill', 'Goryaynov')
print(user.describe_user())

admin = Admin('Ilya', 'Goryaynov')
print(admin.describe_user())
print(admin.privileges.show_privileges())