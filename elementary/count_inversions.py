def count_inversion(sequence):
	count = 0
	j = 0
	for i in range(len(sequence)):
		if sequence[i] < sequence[i-1]:
			while sequence[i] > sequence[i+j]:
				count += 1
				j += 1
	return count
print(count_inversion((1, 2, 5, 3, 4, 7, 6)))
print(count_inversion((0, 1, 2, 3)))