def checkio(num):
	П = 1
	for i in str(num):
		if int(i): П *= int(i)
	return П

print(checkio(123405))
print(checkio(999))
print(checkio(1000))
print(checkio(1111))