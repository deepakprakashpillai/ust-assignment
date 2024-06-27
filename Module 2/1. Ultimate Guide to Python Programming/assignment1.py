with open("./sample.txt","r") as file:
    text = file.read()
    text = text.lower()

    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_text = ''.join(char for char in text if char not in punctuation)
    
    word_freq = {}
    words = cleaned_text.split()
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    top_10 = sorted_word_freq[:10]

    print(top_10)

    