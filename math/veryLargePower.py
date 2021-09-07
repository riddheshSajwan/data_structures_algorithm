'''
Problem Description

Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).

"^" means power ,

"%" means "mod", and

"!" means factorial.



Problem Constraints
1 <= A, B <= 5e5



Input Format
First argument is the integer A

Second argument is the integer B



Output Format
Return one integer, the answer to the problem
'''
def solve(A, B):
        
    def power(x, y, p): 

        res = 1        # Initialize result 
        
        x = x % p      # Update x if it is more than or equal to p 
        
        while (y > 0): 
            # If y is odd, multiply x with result 
            if (y & 1): 
                res = (res * x) % p 
            y = y >> 1 
            x = (x * x) % p
        return res
        
    p = int(1e9+7)
    rem = 1
    while B > 1:
        rem *= B%(p-1)
        B -= 1
        rem %= p-1
    return power(A,rem,p)

print(solve(2, 2))