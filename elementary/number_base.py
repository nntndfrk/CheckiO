def checkio(str_num, base):
	try: return int(str_num, base)
	except ValueError: return -1