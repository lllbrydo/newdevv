age = int(input("Введіть ваш вік "))

if age >= 18 and age <= 150:
    print("Ви дорослий")
elif age < 18 and age > 0:
    print("Ви дитина")
elif age <= 0 or age > 150:
    print("Еррор")
