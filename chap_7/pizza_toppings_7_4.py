topping = "Enter a topping for pizza: "

while True:
    message = input(topping)

    if message == "stop":
        break
    else:
        print(f"Your order is done, pizza with {message} topping")