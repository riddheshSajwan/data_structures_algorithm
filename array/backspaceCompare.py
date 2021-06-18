# https://leetcode.com/problems/backspace-string-compare/

def backspaceCompare(s,t):
    arr1,arr2 = [],[]
    
    for ch in s:
        if ch != '#':
            arr1.append(ch)
        elif arr1:
            arr1.pop()
        
    for ch in t:
        if ch != '#':
            arr2.append(ch)
        elif arr2:
            arr2.pop()
    
    return arr1 == arr2

print(backspaceCompare("ab#c","ad#c"))