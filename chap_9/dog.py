class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def roll_over(self):
        print(f'{self.name} - roll over')

    def sit(self):
        print(f'{self.name} - sit')

    def display_age(self):
        print(f'{self.name} - age is: {self.age}')


my_dog = Dog('Barri', 10)
your_dog = Dog('Robin', 8)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()

my_dog.sit()
my_dog.roll_over()
my_dog.display_age()
