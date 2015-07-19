def checkio(password):
	if len(password) >= 10:
		l = []
		for i in range(len(password)):
			l.append(password[i].split())
		c1, c2, c3 = 0, 0, 0
		s = ''
		for item in l:
			if (s.join(item)).isdigit():
				c1 += 1
			elif (s.join(item)).islower():
				c2 += 1
			elif (s.join(item)).isupper():
				c3 += 1
		return bool(c1*c2*c3)
	else:
		return False
if __name__ == '__main__':
	print(checkio('A1213pokl'))
	print(checkio('bAse730onE')	)
	print(checkio('asasasasasasasaas'))
	print(checkio('QWERTYqwerty'))
	print(checkio('123456123456'))
	print(checkio('QwErTy911poqqqq'))