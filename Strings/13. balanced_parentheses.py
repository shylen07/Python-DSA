# Question: Check if a string has balanced parentheses.
# Created by Devender Singh

def is_balanced_parentheses(s):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    
    return not stack

# Driver code
input_str = "{[()()]}"
if is_balanced_parentheses(input_str):
    print("Balanced parentheses")
else:
    print("Unbalanced parentheses")
