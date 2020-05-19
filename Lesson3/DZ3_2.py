def user_data(name, surname, year_of_birth, city, email, phone):
    res = f"{name} {surname}, {year_of_birth}, {city}, {email}, {phone}"
    return res


user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_year = input("Введите год рождения: ")
user_city = input("Введите город: ")
user_email = input("Введите электронный адрес: ")
user_phone = input("Введите телефон: ")
print(user_data(surname=user_surname, name=user_name,  year_of_birth=user_year, city=user_city, phone=user_phone,
                email=user_email))
