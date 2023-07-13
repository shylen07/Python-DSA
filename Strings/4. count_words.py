# Question: Count the number of words in a sentence.
# Created by Devender Singh

def count_words(sentence):
    words = sentence.split()
    return len(words)

# Driver code
input_sentence = "This is a sample sentence."
print("Number of words:", count_words(input_sentence))
