viewing_one_exhibit = 5
hours_per_day = 8
exhibit_per_day = hours_per_day * 60 // viewing_one_exhibit
number_of_years = int(input("Введите количество лет: "))
number_of_exhibits = int(input("Введите количество экспонатов: "))
print("За указанное количество лет удастся посмотреть", number_of_years * 365 * exhibit_per_day, "экспонатов")
print("Чтобы посмотреть указанное количество экспонатов, потребуется", number_of_exhibits // exhibit_per_day + 1, "дней")