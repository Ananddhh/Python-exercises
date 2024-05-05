input_sentence = input("Enter a sentence: ")
word_count = 1
for char in input_sentence:
    if char == ' ':
        word_count += 1
print("Number of words in the sentence:", word_count)
