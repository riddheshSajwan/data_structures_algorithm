'''https://www.interviewbit.com/problems/ways-to-form-max-heap/'''

from math import log
class Solution:

    def combination(self,n,r):
        if r > n//2:
            r = n-r
        num = n
        den = 1
        for i in range(1,r):
            num *= (n-i)
            den *= (i+1)
        return num//den
        
    def solve(self, n):
        if n <= 2:
            return 1
        h = int(log(n, 2))
        m = pow(2, h)
        p = n - (m - 1)

        if p >= m // 2:
            L = m - 1
        else:
            L = m - 1 - (m // 2 - p)

        R = n - 1 - L
        return self.combination(n-1,L)*self.solve(L)*self.solve(R)%int(1e9+7)

print(Solution().solve(10))