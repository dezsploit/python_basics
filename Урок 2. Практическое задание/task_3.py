"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
xlist = ['winter', 'spring', 'summer', 'autumn']
xdict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(xdict.get(1))
        print(xlist[0])
elif month == 3 or month == 4 or month ==5:
    print(xdict.get(2))
    print(xlist[1])
elif month == 6 or month == 7 or month == 8:
    print(xdict.get(3))
    print(xlist[2])

elif month == 9 or month == 10 or month == 11:
    print(xdict.get(4))
    print(xlist[3])
