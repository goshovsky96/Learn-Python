# Створення прикладних програм на мові Python
# Лабораторна робота №4
# Гошовський Іван, №Заліковки
print ('[1] Створення прикладних програм на мові Python, Лабораторна #4.1')
print ('[2] Гошовський Іван, №Заліковки')
N = int(input ('[3]	Введіть число: '))
proste = 0
while  proste < N:
	x = 0
	for j in range(1,proste+1):
		if proste % j == 0:
			x += j
	if x-1 == proste:
		print(proste, end = ' ')
	proste += 1
