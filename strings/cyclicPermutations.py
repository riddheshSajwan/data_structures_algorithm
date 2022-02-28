'''
Problem Description
Given two binary strings A and B, count how many cyclic permutations of B when taken XOR with A give 0.
NOTE: If there is a string, S0, S1, ... Sn-1 , then it's cyclic permutation is of the form Sk, Sk+1, ... Sn-1, S0, S1, ... Sk-1 where k can be any integer from 0 to N-1.

Problem Constraints
1 ≤ length(A) = length(B) ≤ 105

Input Format
First argument is a string A.
Second argument is a string B.

Output Format
Return an integer denoting the required answer.

Example Input
Input 1:
 A = "1001"
 B = "0011"
Input 2:
 A = "111"
 B = "111"

Example Output
Output 1:
 1
Output 2:
 3

Example Explanation
Explanation 1:
 4 cyclic permutations of B exists: "0011", "0110", "1100", "1001".  
 There is only one cyclic permutation of B i.e. "1001" which has 0 xor with A.
Explanation 2:
 All cyclic permutations of B are same as A and give 0 when taken xor with A. So, the ans is 3.
 '''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def getZarr(self, string, z, n):
        l, r, k = 0, 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        return z

    def getPeriod(self, z, n):
        for i in range(1,n):
            if z[i] + i == n:
                return i
        return n

    def solve(self, A, B):
        res = 0
        n = len(A)
        z = [0 for i in range(2*n)]
        new_B = B+B
        z = self.getZarr(new_B,z,2*n)
        period = self.getPeriod(z,2*n)
        i,j = 0,n-1
        #print(new_B,z,period)
        while(True):
            while j < 2*n and new_B[i] != A[0]:
                i += 1 
                j += 1
            if j == 2*n: return 0
            if new_B[i:j+1] == A:
                break
            i += 1
            j += 1
        while 2*n - i > n:
            res += 1
            i += period
        return res

print(Solution().solve("1001", "0011"))