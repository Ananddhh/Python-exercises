sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)


# import re

# sentence = input("Enter a sentence: ")
# words = re.findall(r'\b\w+\b', sentence)
# longest_word = max(words, key=len)
# print("Longest word:", longest_word)

# sentence = input("Enter a sentence: ")
# longest_word = max(sentence.split(), key=len)
# print("Longest word:", longest_word)
