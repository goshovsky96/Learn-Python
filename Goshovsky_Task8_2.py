# Створення прикладних програм на мові Python
# Лабораторна робота №7
# Гошовський Іван, №6
def show_x(*x):
	print('x = ',end='')
	for a in x:
		print(a,end=' ')
	print()

def show_y(**y):
	print('y = ',end='')
	for b in y:
		print(y[b],end=' ')
	print()

def f_sum(*x,**y):
	a = []
	b = []
	suma = 0
	for n in x:
		a.append(n)
	for m in y:
		b.append(y[m])
	for i in range(len(a)):
		suma += a[i]**2 + b[i]**2 + a[i]*b[i]
	return suma

kort = (1,2,3,4)
slovn = {
		'one':3,
		'two':4,
		'three':5,
		'four':6
		}
show_x(*kort)
show_y(**slovn)
print('f =',f_sum(*kort,**slovn))