age_prompt = "Enter your age to enter the park (or type 'quit' to exit): "

active = True
while active:
    input_age = input(age_prompt)
    if input_age == 'quit':
        active = False
    else:
        age = int(input_age)

        if age < 3:
            print("Your ticket is free")
        elif 3 <= age <= 12:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15")
