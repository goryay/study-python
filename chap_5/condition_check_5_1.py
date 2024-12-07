cars = ['audi', 'bmw', 'toyota', 'subaru', 'mazda', 'lada', 'tesla', 'mercedes', 'ford', 'cadillac']

car = 'subaru'
print(f"Is car == 'subaru'? I prefer True.")
print(car == 'subaru')

print(f"\nIs car == 'audi'? I prefer False.")
print(car == 'audi')

car = 'BMW'
print(f"\nIs car == 'bmw'? I prefer True.")
print(car.lower() == 'bmw')

print('tesla' in cars)
print('honda' in cars)
print('\n')

age_0 = 12
age_1 = 22
print(age_0 >= 10 and age_1 >= 20)
print(age_0 < 10 or age_1 < 20)