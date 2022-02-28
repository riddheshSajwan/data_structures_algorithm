'''
Problem Description
Given an array of integers A .
value of a array = max(array) - min(array).
Calculate and return the sum of values of all possible subarrays of A % 109+7.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 1000000

Input Format
The first and only argument given is the integer array A.
Output Format
Return the sum of values of all possible subarrays of A % 10^9+7.

Example Input
Input 1:
 A = [1]
Input 2:
 A = [4, 7, 3, 8]

Example Output
Output 1:
 0
Output 2:
 26

Example Explanation
Explanation 1:
Only 1 subarray exists. Its value is 0.
Explanation 2:
value ( [4] ) = 4 - 4 = 0
value ( [7] ) = 7 - 7 = 0
value ( [3] ) = 3 - 3 = 0
value ( [8] ) = 8 - 8 = 0
value ( [4, 7] ) = 7 - 4 = 3
value ( [7, 3] ) = 7 - 3 = 4
value ( [3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3] ) = 7 - 3 = 4
value ( [7, 3, 8] ) = 8 - 3 = 5
value ( [4, 7, 3, 8] ) = 8 - 3 = 5
sum of values % 10^9+7 = 26
'''

def solve(A):
    n = len(A)
    min_stack,max_stack = [],[]
    res_sum = 0
    MOD = int(1e9+7)
    left_min,left_max = [],[]
    right_min,right_max = [n for i in range(n)],[n for i in range(n)]
    for i in range(n):
        while min_stack and A[min_stack[-1]] >= A[i]:
            min_stack.pop()
        if min_stack == []:
            left_min.append(-1)
        else:
            left_min.append(min_stack[-1])
        min_stack.append(i)
        while max_stack and A[max_stack[-1]] <= A[i]:
            max_stack.pop()
        if max_stack == []:
            left_max.append(-1)
        else:
            left_max.append(max_stack[-1])
        max_stack.append(i)
    
    min_stack.clear(),max_stack.clear()

    for i in range(n-1,-1,-1):
        while min_stack and A[min_stack[-1]] >= A[i]:
            min_stack.pop()
        if min_stack:
            right_min[i] = min_stack[-1]
        min_stack.append(i)
        while max_stack and A[max_stack[-1]] <= A[i]:
            max_stack.pop()
        if max_stack:
            right_max[i] = max_stack[-1]
        max_stack.append(i)
    #right_min.reverse(),right_max.reverse()
    for i in range(n):
        res_sum = (res_sum + A[i]*((i-left_max[i])*(right_max[i]-i)-(i-left_min[i])*(right_min[i]-i)))%MOD
    #print(left_min,left_max,right_min,right_max)
    return res_sum%MOD

print(solve([4, 7, 3, 8]))