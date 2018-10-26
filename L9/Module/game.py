from gameModule import *
x = int(input('Загадай число (1-5): '))
result,num = ugadaika(x)
if result:
	print('Ура! {} - правильне число'.format(num))
else:
	print('Не вгадали. Це було число -', num)
