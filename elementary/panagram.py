def check_pangram(text):
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
    text = text.upper()
    checks = []
    check = True
    for item in alphabet:
        if item in text:
            checks.append(True)
        else:
            checks.append(False)
    for item in checks:
        check *= item
    return bool(check)

print(check_pangram("The quick brown fox jumps over the lazy dog."))
print(check_pangram("ABCDEF."))