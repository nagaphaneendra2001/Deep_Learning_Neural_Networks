def count_word():
    file1 = open("input.txt", "r")
    info = file1.read().split("\n")  # Using split to get a list of words
    file2 = open("output.txt", "w")
    for sentence in info:
        sentence = sentence + "\n"
        file2.write(sentence)
    #print(info)
    file1.close()
    file2.write("Word_Count: \n")
    word_count = {}
    for line in info:
        words = line.strip().split(" ")
        #print(x)
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    print("word_count:")
    print(word_count)
    for word, count in word_count.items():
        entry = "\n" + word + " " + str(count)
        file2.write(entry)

    file2.close()

count_word()
