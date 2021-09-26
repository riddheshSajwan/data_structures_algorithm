'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

def letterCombinations(A):
    letter_pad = {'0':['0'],'1':['1'],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                    '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],
                    '9':['w','x','y','z']}
    res = []
    n = len(A)
    if n == 0:
        return []
    def _solve(index1,_res):
        if len(_res) == n:
            res.append(_res)
            return
        for i in range(index1,n):
            digit = letter_pad[A[i]]
            for j in range(len(digit)):
                _solve(i+1,_res+digit[j])
    _solve(0,"")
    return res
print(letterCombinations("23"))