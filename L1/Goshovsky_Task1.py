cours_name = 'Створення прикладних програм на мові Python'
lab_num = 1
print ('[1] ' + cours_name, lab_num, sep = ', ')

name = 'Ivan'
surname = 'Goshovsky'
var_num = 'NUM-12345'
print ('[2] ' + name + ' ' + surname, var_num, sep = ', ')

teacher = 'Ivan Yaroslavovich'
result = '[3] '
for i in range(45):
	if i == 0:
		result += teacher
	else:
		result += ', ' + teacher
print (result)

x = 7.8 - (1+2.1/3)/(78+21.3)
print('[4] x = ', x)
