'''
Problem Description

Given a positive integer A, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 


Problem Constraints
1 <= A <= 109

Input Format
First and only argument of input contains single integer A

Output Format
Return a string denoting the corresponding title.
'''

def convertToTitle(A):
    def get_title(n):
        if n == 0: return 'Z'
        return chr(ord('A')+n-1)
    res = ""
    while A > 26:
        rem = A%26
        A //= 26
        if rem == 0: 
            rem = 26
            A -= 1
        res = get_title(rem) + res
    
    return get_title(A) + res

print(convertToTitle(27))