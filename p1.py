def word_count(filename):
    file = open(filename, 'r')
    words = file.read().split()
    word_freq = {}
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    file.close()
    return word_freq
