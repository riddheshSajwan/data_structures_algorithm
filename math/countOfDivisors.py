'''
https://www.geeksforgeeks.org/total-number-divisors-given-number/
'''
def solve(A):
    mx, p = max(A), 2
    prime = [-1] * (mx + 1) #Stores the smallest prime factor of integers 1 to max(A)
    while p * p <= mx:
        if prime[p] == -1:
            prime[p] = p
            for i in range(p * p, mx + 1, p):
                if prime[i] == -1:
                    prime[i] = p
        p += 1
    ans = []
    #Using prime factorization to get the number of divisors for every integer
    for i in A:
        if i == 1:
            ans.append(1)
            continue
        num, num_of_divisors = i, 1
        while num > 1:
            cnt = 0
            temp = prime[num]
            while num > 1 and num % temp == 0:
                num //= temp
                cnt += 1
            num_of_divisors *= (cnt + 1)
        ans.append(num_of_divisors)
    return ans

print(solve([2, 3, 4, 5]))