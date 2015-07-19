def checkio(str1, str2):
	ls1 = str1.split(",")
	ls2 = str2.split(",")
	ls = []
	for i in ls1:
		for j in ls2:
			if i == j:
				ls.append(i)
	return ','.join(ls)


print(checkio("hello,world", "hello,earth"))
print(checkio("one,two,three", "four,five,six"))
print(checkio("one,two,three", "four,five,one,two,six,three"))
