def find_message(text):
    """Find a secret message"""
    l = []
    for item in text:
        if item.isupper():
            l.append(item)
    return ''.join(l)

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
print(find_message("hello world!"))
print(find_message("HELLO WORLD!!!"))