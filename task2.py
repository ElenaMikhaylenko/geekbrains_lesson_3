name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birthday = int(input("Введите год Вашего рождения: "))
city = input("Город проживания: ")
email = input("Введите Вашу электронную почту: ")
telephone = input("Введите Ваш номер телефона: ")

def my_func(**kwargs):

    print(kwargs)

print(my_func(Имя = name,**{"Фамилия": surname, "Год рождения": birthday, "Город": city, "Почта": email,"Телефон": telephone}))