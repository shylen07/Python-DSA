# Question: Reverse the order of words in a sentence.
# Created by Devender Singh

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

# Driver code
input_sentence = "This is a sample sentence."
print("Reversed words:", reverse_words(input_sentence))