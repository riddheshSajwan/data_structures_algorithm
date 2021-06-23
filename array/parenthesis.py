'''
https://leetcode.com/problems/valid-parentheses/submissions/
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
    return stack == []

print(isValid("{([])}"))