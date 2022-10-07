name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")
print(name + "_" + surname + "_" + year)
name, surname = surname, name
year = str(int(year) + 60)
print(name + "_" + surname + "_" + year)
