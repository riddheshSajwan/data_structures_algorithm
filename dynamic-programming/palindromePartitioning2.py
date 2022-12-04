'''
https://leetcode.com/problems/palindrome-partitioning-ii/description/
'''

def minCut(s):
    def is_palindrome(string): 
        return string == string[::-1]
    
    dp = [0]*(len(s)+1) 
    for k in range(1, len(dp)):
        if is_palindrome(s[:k]):
            dp[k] = 0 
        else:            
            dp[k] = dp[k-1] + 1
            for j in range(k-1, -1, -1):
                dp[k] = min(dp[k], dp[j] + 1 + int(not(is_palindrome(s[j:k])))*len(s[j:k]))
    return dp[-1]

print(minCut("aab"))
