def count_words(text, words):
    ans=0
    for i in words:
        if i in text.lower():
            ans+=1
    return ans 
print(count_words("How aresjfhdskfhskd you?",
	 {"how", "are", "you", "hello"}))
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.", {"sum", "hamlet", "infinity", "anything"}))