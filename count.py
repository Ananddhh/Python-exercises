input_sentence = input("Enter a sentence: ")
word_count = 1
for char in input_sentence:
    if char == ' ':
        word_count += 1
print("Number of words in the sentence:", word_count)



# def count_words(sentence):
#     word_count = 0
#     is_word = False
#     for char in sentence:
#         if char != ' ' and not is_word:
#             word_count += 1
#             is_word = True
#         elif char == ' ':
#             is_word = False
#     return word_count

# input_sentence = input("Enter a sentence: ")
# print("Number of words in the sentence:", count_words(input_sentence))
