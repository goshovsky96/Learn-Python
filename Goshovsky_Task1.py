# у першому рядку назву курсу та номер лабораторної роботи
cours_name = 'PMM-2'
lab_num = 1
print ('[1] ' + cours_name, lab_num, sep = ', ')

# у другому - ваше ім’я та прізвище, а також номер Вашої заліковки. 
name = 'Ivan'
surname = 'Goshovsky'
var_num = 'NUM-12345'
print ('[2] ' + name + ' ' + surname, var_num, sep = ', ')

# у третьому – сорок п’ять разів через кому з пробілом ім’я
# викладача цих практичних занять (подумайте, як зробити так,
# щоб останнє ім’я не закінчувалось комою)
teacher = 'Ivan Yaroslavovich'
result = '[3] '
for i in range(45):
	if i == 0:
		result += teacher
	else:
		result += ', ' + teacher
print (result)

# Використовуючи інтерпретаторі Python обчислити наступні вирази
# згідно варіанта індивідуального завдання: (v6)
x = 7.8 - (1+2.1/3)/(78+21.3)
print('[4] x = ', x)