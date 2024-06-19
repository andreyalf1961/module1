#задание по теме: "Изменяемые и неизменяемые объекты. Кортежи и списки."

immutable_var='apple',5,9,8, False
print(immutable_var)
#immutable_var[0]='banana'  кортеж не поддерживает подобное изменение

mutable_list=['apple',5,9,8, True]
print(mutable_list)
mutable_list[0]='banana'
print(mutable_list)