def boolean(x, y, operation):
	
	operations = ["conjunction", "disjunction",
	 "implication", "exclusive", "equivalence"]
	
	if operation in operations:
		if operation == "conjunction":
			return x and y
		elif operation == "disjunction":
			return x or y
		elif operation == "implication":
			if x:
				return y
			else:
				return not(x)
		elif operation == 'exclusive':
			if x:
				return not(y)
			else:
				return y
		elif operation == "equivalence":
			if x:
				return y
			else:
				return not(y)
		else: return None
	else: return None



print(boolean(1, 0, "conjunction"))
print(boolean(0, 1, "exclusive"))