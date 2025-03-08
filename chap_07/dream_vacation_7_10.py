vacations = {}
vacation_active = True
while vacation_active:
    name = input("What is your name? ")
    vacation = input("What is your dream vacation? ")
    vacations[name] = vacation

    repeat = input("Would you like to continue (yes/no)? ")
    if repeat == "no":
        vacation_active = False

print(f"Finish")
for name, vacation in vacations.items():
    print(f"{name} : {vacation}")