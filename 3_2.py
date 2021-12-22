def character():
    name = input('Имя ')
    surname = input('фамилия ')
    age = input('год рождения ')
    city = input('город ')
    mail = input('почта ')
    phone = input('телефон ')
    return f'{name} {surname}, {age}г., г. {city}, тел. {phone}, email: {mail}'


print(character())
