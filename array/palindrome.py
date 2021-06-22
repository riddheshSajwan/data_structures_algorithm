'''
https://leetcode.com/problems/valid-palindrome/
'''
import re

def isPalindrome(s):
    s = re.sub('[^a-z0-9]', '', s.lower())
    i = 0
    while i < len(s)//2:
        if s[i] == s[-(i+1)]:
            i += 1
        else:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))