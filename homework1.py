#Строки и индексация строк
example='реакция'
print(example[0])
print(example[-1])
print(example[4:])
print(example[::-1])
print(example[1::2])
a=((len(example))/2) #другое решение пункта 4
a=(round(a))
print(example[a:])