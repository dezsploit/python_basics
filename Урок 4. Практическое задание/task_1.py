"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
def plata():
    try:
        time = float(input('Выработка в часах: '))
        salary = float(input('Ставка в час: '))
        bonus = float(input('Премия: '))
        result = time * salary + bonus
        print(f'Итого  {result}')
    except ValueError:
        return print('Неверное значение')
plata()
