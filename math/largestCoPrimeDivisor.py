'''
Problem Description

You are given two positive numbers A and B . You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1


Problem Constraints
1 <= A, B <= 109



Input Format
First argument is an integer A.
Second argument is an integer B.



Output Format
Return an integer maximum value of X as descibed above.
'''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def cpFact(A, B):
    x = 1
    res = float('-inf')
    while x <= int(pow(A,0.5)):
        if A%x == 0 :
            if gcd(A//x,B) == 1:
                return A//x
            elif gcd(x,B) == 1:
                res = max(res,x)
        x += 1
    return res

def cpFact2(A,B):    
    #best solution
    while(gcd(A, B) != 1):
        A = A / gcd(A, B)
    return int(A)    

print(cpFact(30, 12))
print(cpFact2(30, 12))