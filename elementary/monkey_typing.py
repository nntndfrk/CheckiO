def count_words(text, words):
    text = text.lower()
    list1 = text.split(' ')
    list2 = []
    for item in words:
        list2.append(item)
    count = 0
    for i in list2:
        for j in list1:
            if i in j:
                count += 1
                break
    return count
print(count_words("How aresjfhdskfhskd you?",
	 {"how", "are", "you", "hello"}))
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
         {"sum", "hamlet", "infinity", "anything"}))
