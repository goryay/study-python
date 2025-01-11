class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def fullname(self):
        first = self.first
        last = self.last
        print(first + ' ' + last)

    def read_raise(self):
        print(f"Твой оклад на данный момент - {self.salary}")

    def give_raise(self, percent):
        result_of_the_year = self.salary * (1 + percent)
        print(f"Твой оклад в конце года - {result_of_the_year}")

