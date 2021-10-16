'''
Sorted Permutation Rank with Repeats
Problem Description

Given a string A, find the rank of the string amongst its permutations sorted lexicographically. Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. Look at the example for more details.

NOTE:

The answer might not fit in an integer, so return your answer % 1000003 where 1000003 is a prime number.
String A can consist of both lowercase and uppercase letters. Characters with lesser ascii value are considered smaller i.e. 'a' > 'Z'.
'''
def findRank(A):
    n = len(A)
    s = sorted(set(A))
    #print(s)
    rank = 0
    def fact(n):
        res = 1
        for i in range(1,n+1):
            res *= i
        return res
    freq_map = {}
    for item in A:
        if item not in freq_map:
            freq_map[item] = 0
        freq_map[item] += 1
    for i in range(n):
        cnt = 0
        for j in s:
            if j == A[i]: break
            if freq_map[j] > 0:
                freq_map[j] -= 1
                den = 1
                for key in freq_map:
                    if freq_map[key] > 1:
                        den *= fact(freq_map[key])
                #print(freq_map,den)
                rank += fact(n-1-i)//den
                freq_map[j] += 1
        freq_map[A[i]] -= 1
    return (rank+1)%1000003

print(findRank("babca"))