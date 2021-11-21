def longestUniqueSubsttr(S):
    # code here
    cache = set()
    left = 0
    right = 0
    maxLen = 0
    while right < len(S):
        while S[right] in cache:
            cache.remove(S[left])
            left += 1
        
        cache.add(S[right])
        maxLen = max(maxLen,right-left+1)
        right += 1
            
    return maxLen
print(longestUniqueSubsttr("zyaaabcdefghijklmnopqrstuvwxyzgffg"))