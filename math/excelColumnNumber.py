'''
Problem Description

Given a column title as appears in an Excel sheet, return its corresponding column number.



Problem Constraints
1 <= length of the column title <= 5



Input Format
Input a string which represents the column title in excel sheet.



Output Format
Return a single integer which represents the corresponding column number.
'''

def titleToNumber(A):
    def get_number(alphabet):
        return ord(alphabet)-ord('A')+1
    exp = 0
    res = 0
    for ch in A[::-1]:
        res += pow(26,exp)*get_number(ch)
        exp += 1
    return res

print(titleToNumber("ABCD"))
    