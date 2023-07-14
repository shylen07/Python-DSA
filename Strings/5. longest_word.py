# Question: Find the longest word in a sentence.
# Created by Devender Singh

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Driver code
input_sentence = "The quick brown fox jumps over the lazy dog."
print("Longest word:", longest_word(input_sentence))