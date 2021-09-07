'''
Problem Description

Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.



Problem Constraints
4 <= A <= 2*107



Input Format
First and only argument of input is an even number A.



Output Format
Return a integer array of size 2 containing primes whose sum will be equal to given number.
'''
def primesum(A):
    sieve_arr = [True for i in range(A+1)]
    p = 2
    while p*p <= A:
        if sieve_arr[p]:
            for i in range(p*p,A+1,p):
                sieve_arr[i] = False
        p += 1
    
    i = 2
    while i <= A//2:
        if sieve_arr[i] and sieve_arr[A-i]:
            return [i,A-i]
        i += 1
    
print(primesum(9))