class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        return f'{self.first_name} {self.last_name}'

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'You have {self.login_attempts} login attempts.')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'You have {self.login_attempts} login attempts.')


# user_info = User('Ilya', 'Goryaynov')
# user_info.increment_login_attempts()
# user_info.increment_login_attempts()
# user_info.increment_login_attempts()
# user_info.reset_login_attempts()
# user_info.describe_user()

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ['You can add message', 'You can delete users', 'You can ban users']
        else:
            self.privileges = privileges

    def show_privileges(self):
        privileges_str = "Privileges:\n"
        for privilege in self.privileges:
            privileges_str += f"{privilege}\n"
        return privileges_str.strip()

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

# user_rules = Admin('Ilya', 'Goryaynov')
# user_rules.greet_user()
# user_rules.privileges.show_privileges()