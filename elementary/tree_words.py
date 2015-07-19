def checkio(words):
	L = words.split(' ')
	count = 0
	I = iter(L)
	while True and count < 3:
		try:
			X = next(I)
			if X.isalpha():
				count += 1
			if X.isdigit():
				count = 0
		except StopIteration:
			break
	if count >= 3:
		return True
	else:
		return False	
print(checkio("Hello World hello"))
print(checkio("1 2 3 4"))
print(checkio('as 4 gh jh kj 78'))