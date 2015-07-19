def left_join(phrases):
	l = []
	for item in phrases:
		l.append(item.replace('right', 'left'))
	return ','.join(l)

print(left_join(("left", "right", "left", "stop")))
print(left_join(("bright aright", "ok")))
print(left_join(("brightness wright",)))
print(left_join(("enough", "jokes")))
