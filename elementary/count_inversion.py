def count_inversion(sequence):
    count = 0
    for j in range(len(sequence)):
        for i in range(len(sequence)):
            if j < i and sequence[j] > sequence[i]:
                count += 1
            #else:
              # pass
        j += 1
    return count
print(count_inversion((1, 4, 2, 3, 7, 5, 6)))
print(count_inversion((0, 1, 2, 3)))
            
