'''
https://leetcode.com/problems/longest-string-chain/
'''
def longestStrChain(words):
    d = dict()
    for word in words:
        d[word] = 1
    longest = 1

    for word in sorted(words, key=len):
        for i in range(len(word)):
            prev = word[:i] + word[i + 1:]
            if prev in d:
                d[word] = max(d[word], d[prev] + 1)
        longest = max(longest, d[word])
    return longest
print(longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))