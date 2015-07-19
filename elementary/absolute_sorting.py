
def checkio(num_list):
    clear_list = []
    for item in num_list:
        clear_list.append(item)
    return sorted(clear_list, key=abs)
    
print(checkio((-20, -5, 10, 15)))
print(checkio((1, 2, 3, 0)))
print(checkio((-1, -2, -3, 0)))

