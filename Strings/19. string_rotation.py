# Question: Check if a string is a rotation of another string.
# Created by Devender Singh

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1

# Driver code
string1 = "waterbottle"
string2 = "erbottlewat"
if is_rotation(string1, string2):
    print("String2 is a rotation of String1")
else:
    print("String2 is not a rotation of String1")