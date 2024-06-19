# Задание
# Работа со словарем
my_dict = {'Андрей': 2896, 'Юрий': 1589}
print(my_dict)
print(my_dict.get('Юрий', 'Такого нет'))
print(my_dict.get('Филимон', 'Такого нет'))
my_dict.update({'Петр': 2487, 'Светлана': 4589})
print(my_dict)
a = my_dict.pop('Петр')
print(a)
print(my_dict)

# Работа с множеством
my_set = {'Сорока', 456, 2, 2, 7, 7, True}
print(my_set)
my_set.add(5)  # добавление элемента
my_set.add((1, 2))  # добавление кортежа
print(my_set)
my_set.discard((1, 2))
print(my_set)
my_set.pop()  # не по заданию. Удалился первый элемент.
print(my_set)
