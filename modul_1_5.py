immutable_var=1, 2, 3, True, 'String'
print('immutable_var:', immutable_var)
#immutable_var[0] = 200 # Потому что кортеж - это неизменяемый тип данных
mutable_list=[1, 2, 3, 'q','w','e']
mutable_list[0]=100
mutable_list[1]=20
print('mutable_list:', mutable_list)
