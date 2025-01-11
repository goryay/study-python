from employee import Employee

print("Приветствую! Давайте создадим информацию о сотруднике.")

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
salary = float(input("Введите текущий оклад: "))

employee = Employee(first_name, last_name, salary)

print("\nИнформация о сотруднике:")
employee.fullname()
employee.read_raise()

while True:
    try:
        raise_percent = float(input("\nВведите процент повышения оклада (например, 0.1 для 10%): "))
        if raise_percent < 0:
            print("Процент не может быть отрицательным. Попробуйте снова.")
            continue
        employee.give_raise(raise_percent)
        break
    except ValueError:
        print("Пожалуйста, введите числовое значение.")
