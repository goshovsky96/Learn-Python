from random import randint
def ugadaika(num):
	n = randint(1,5)
	if num == n:
		return True, n
	else:
		return False, n