from math import factorial, pow
def  fgen(x,eps):
  k = 2
  second = (pow(-1,0)*pow(x,2*0))/factorial(2*0)
  yield second
  first = (pow(-1,1)*pow(x,2*1))/factorial(2*1)
  er = abs(second - first)
  while (er > eps):
    yield first
    k += 1
    second = first
    first = (pow(-1,k)*pow(x,2*k))/factorial(2*k)
    er = abs(second - first)
  yield first
sp = [x for x in fgen(6,0.1)]
suma = 0
for x in sp: suma += x
print(sp)
print('Сума = ', suma)