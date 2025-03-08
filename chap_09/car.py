class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer_reading(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer_reading(self, mileage_reading):
        if mileage_reading >= self.odometer_reading:
            self.odometer_reading = mileage_reading
        else:
            print("You can't do that!")

    def increment_odometer_reading(self, mileage_reading):
        if mileage_reading > 0:
            self.odometer_reading += mileage_reading
        else:
            print("Mileage to increment must be positive.")


my_new_car = Car('subaru', 'outback', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer_reading()
my_new_car.update_odometer_reading(40)
my_new_car.read_odometer_reading()
my_new_car.increment_odometer_reading(0)
my_new_car.read_odometer_reading()


class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} percent battery.")

    def get_range(self):
        if self.battery_size == 100:
            range = 240
        elif self.battery_size == 150:
            range = 700

        print(f"This car can go about {range} miles on it.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has {self.battery} percent battery.")

    def fill_gas_tank(self):
        print(f"This car does not have any gas tanks.")

my_new_electric_car = ElectricCar('tesla', 'hatchback', 2024)
print(my_new_electric_car.get_descriptive_name())
my_new_electric_car.battery.describe_battery()
my_new_electric_car.battery.get_range()
