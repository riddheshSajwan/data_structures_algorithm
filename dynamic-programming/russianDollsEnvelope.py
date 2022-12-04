'''
https://leetcode.com/problems/russian-doll-envelopes/description/
'''

def maxEnvelopes(A):
    v = []
    n = len(A)
    for i in range(0, n):
        v.append((A[i][0], -A[i][1]))

    # sort the vector envelope in increasing order of heights
    v.sort()
    dp = [0] * n
    dp[0] = 1

    # Find the longest increasing subsequence based on second element of v[i]
    for i in range(1, n):
        dp[i] = 1
        for j in range(i - 1, -1, -1):
            if v[j][0] < v[i][0] and v[j][1] > v[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

envelopes = [[5,4],[6,4],[6,7],[2,3]]

print(maxEnvelopes(envelopes))