years = int(input("Enter years: "))

if years < 2:
    print("Infant")
elif years >= 2 and years < 4:
    print("Baby")
elif years >= 4 and years < 13:
    print("Child")
elif years >= 13 and years < 20:
    print("Teenager")
elif years >= 20 and years < 65:
    print("Adult")
else:
    print("Elderly person")
