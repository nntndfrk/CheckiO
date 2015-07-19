def checkio(words):
    for item in words:
        for word in words:
            if word != item and word.endswith(item):
                return True
    else:
                return False
    
print(checkio({"hello", "lo", "he"}))
print(checkio({"hello", "la", "hellow", "cow"}))
print(checkio({"walk", "duckwalk"}))
