"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [list1[i] for i in range(1,len(list1)-1) if list1[i] > list1[i-1]]
print(list2)


import random
list1 = random.sample(range(1, 300), 13) 
print(list1)
list2 = []
for el in range(len(list1) - 1):
    if list1[el] < list1[el+1]:
        list2.append(list1[el+1])
print(list2)
