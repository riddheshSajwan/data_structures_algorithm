'''
https://www.geeksforgeeks.org/lexicographic-rank-of-a-string/
'''

def findRank(A):
    '''
    store less_than value of each element in a map
    iterate over A and calculate the perms before every element by using -
        rank += less_than_count[element] * (len(A)-1-index(element))!
    return rank
    '''
    n = len(A)
    s = sorted(A)
    rank = 0
    def fact(n):
        res = 1
        for i in range(1,n+1):
            res *= i
        return res
    visited = set()
    for i in range(n):
        cnt = 0
        for j in s:
            if j == A[i]: break
            if j not in visited: cnt += 1
            
        rank += cnt * fact(len(A)-1-i)
        visited.add(A[i])
    return (rank+1)%1000003

print(findRank("acb"))