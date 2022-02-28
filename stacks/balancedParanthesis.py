'''
https://leetcode.com/problems/valid-parentheses/
'''

def isValid(s):
    complement = {')':'(','}':'{',']':'['}
    stack = []
    for brace in s:
        braceComplement = complement.get(brace)
        if stack and braceComplement == stack[-1]:
            stack.pop()
        else:
            stack.append(brace)
    return 1 if stack == [] else 0

s = "()[]{}"
print(isValid(s))