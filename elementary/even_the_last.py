def checkio(array):
	if len(array) > 0:
		p_array = array[::2]
		return sum(p_array) * array[len(array)-1]
	else:
		return 0
print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))
