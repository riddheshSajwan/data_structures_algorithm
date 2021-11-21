'''
https://leetcode.com/problems/valid-palindrome-ii/
'''
def almostPalindrome(s):
      
    def isPalindrome(s):
        i = 0
        while i < len(s)//2:
            if s[i] != s[-(i+1)]:
                return False
            i += 1
        return True
    
    i = 0
    size = len(s)
    while i < size//2:
        if s[i] != s[-(i+1)]:
            return isPalindrome(s[i:size-i-1]) or isPalindrome(s[i+1:size-i])
        i += 1
    return True

print(almostPalindrome("abc"))