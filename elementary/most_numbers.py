def checkio(*args):
	if args:
		return(max(*args) - min(*args))
	else:
		return 0
print(checkio(1, 2, 3))
print(checkio(5, -5))
print(checkio(10.2, -2.2, 0, 1.1, 0.5))
#print(checkio(), 0, 3))