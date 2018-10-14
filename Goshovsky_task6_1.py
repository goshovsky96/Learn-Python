# Створення прикладних програм на мові Python
# Лабораторна робота №6_1
# Гошовський Іван, №6
spis = []
val = input('Введіть числа через пробіл: ')
for x in map(int, val.split()):
	spis.append(x)
n = len(spis)
for k in range(n):
	if k!=n-1: 
		print (spis[n-k-1], end=' ')
	else:
		print (spis[n-k-1])
print ('Готово!')