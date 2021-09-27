'''
https://leetcode.com/problems/combinations/
'''
def combine(A, B):
    res = []
    def _combine(l,r,rem,_res):
        if rem == 0:
            res.append(_res)
            return
        for i in range(l,r):
            _combine(i+1,r,rem-1,_res+[i])
    _combine(1,A+1,B,[])
    return res

print(combine(4, 2))