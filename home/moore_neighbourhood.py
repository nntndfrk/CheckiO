"""пофіксити вихід за межі тюпла!! - це типу пофіксив, 
але тепер якось невірно рахує =(("""

def count_neighbours(*grid):
	if grid[0][grid[1]][grid[2]]:
		count = -1
	else:
		count = 0
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			if grid[1]+j >= 0 and grid[2]+i >= 0:
				try:
					if grid[0][grid[1]+j][grid[2]+i]:
						count += 1
				except IndexError:
					break
			else: pass
	return count

if __name__ == '__main__':
	print(count_neighbours(((1, 0, 0, 1, 0),

                  (0, 1, 0, 0, 0),

                  (0, 0, 1, 0, 1),

                  (1, 0, 0, 0, 0),

                  (0, 0, 1, 0, 0),), 1, 2))
	print(count_neighbours(((1, 0, 0, 1, 0),

                  (0, 1, 0, 0, 0),

                  (0, 0, 1, 0, 1),

                  (1, 0, 0, 0, 0),

                  (0, 0, 1, 0, 0),), 0, 0))
	print(count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2))

	print(count_neighbours(((1, 0, 0),
                             (0, 1, 0),
                             (0, 1, 0),), 1, 1))
