# Створення прикладних програм на мові Python
# Лабораторна робота №6_3
# Гошовський Іван, №6
def search_ind(text):
	"""Шукає індекс першої ind[0] та останньої ind[1] літери h (H)
		Якщо літера h (H) в рядку одна - то ind[0] = ind[1]
		Якщо в рядку немає літери h (H) - то ind[0] = len(text), ind[1] = 0
	"""
	ind = [0,len(text)]
	for t in text:
		if (t == 'h' or t == 'H'):
			break 
		ind[0] += 1

	for i in range(len(text)):
		if text[len(text)-i-1] == 'h' or text[len(text)-i-1] == 'H':
			break
		ind[1] = len(text)-i-2
	return ind

def out_text(text:str,ind:list):
	if ind[0] == len(text) and ind[1] == -1:
		return(text)
	elif ind[0] == ind[1]:
		return(text[0:ind[0]])
	else:
		return(text[0:ind[0]]+text[ind[1]+1:]) 
s = input('Введіть текст:')
index = search_ind(s)

print('Кількість літер в рядку:',len(s))
print('Індекси: 1 літера - {}, остання - {}'.format(index[0],index[1]))
print('Результат:', out_text(s,index))
