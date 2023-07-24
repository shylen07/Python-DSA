# Question: Capitalize the first letter of each word in a sentence.
# Created by Devender Singh

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

# Driver code
input_sentence = "this is a sample sentence."
print("Capitalized sentence:", capitalize_words(input_sentence))
