class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'You have {self.login_attempts} login attempts.')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'You have {self.login_attempts} login attempts.')


user_info = User('Ilya', 'Goryaynov')
user_info.increment_login_attempts()
user_info.increment_login_attempts()
user_info.increment_login_attempts()
user_info.reset_login_attempts()
user_info.describe_user()
user_info.greet_user()