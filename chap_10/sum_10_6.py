while True:
    print(f"Enter 'q' to quit.")
    num1, num2 = input(f"Enter first number: "), input(f"Enter second number: ")
    if num1 == 'q' or num2 == 'q':
        break
    try:
        res = int(num1) + int(num2)
    except ValueError:
        pass
        # print("Invalid input")
    else:
        print(f"The sum of {num1} and {num2} is {res}.")
