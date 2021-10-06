'''
https://leetcode.com/problems/word-break-ii/
'''

def wordBreak(s, wordDict):
    memo = {len(s): ['']}
    def sentences(i):
        if i not in memo:
            memo[i] = [s[i:j] + (tail and ' ' + tail)
                        for j in range(i+1, len(s)+1)
                        if s[i:j] in wordDict
                        for tail in sentences(j)]
        return memo[i]
    return sentences(0)

A = "catsanddog"
B = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(A, B))