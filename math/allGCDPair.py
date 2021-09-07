'''
https://www.geeksforgeeks.org/find-original-numbers-from-gcd-every-pair/
'''

def solve(arr):
    def gcd(a,b):
        if a == 0 :
            return b
        return gcd(b%a,a)
    n = len(arr)
    arr.sort(reverse = True)

    freq = [0 for i in range(arr[0] + 1)]
    
    # Count frequency of each element
    for i in range(n):
        freq[arr[i]] += 1
    
    # Size of the resultant array
    brr = [0 for i in range(len(arr))]
    l = 0
    
    for i in range(n):
        if (freq[arr[i]] > 0):
                
            # Store the highest element in
            # the resultant array
            brr[l] = arr[i]
    
            # Decrement the frequency of that element
            freq[brr[l]] -= 1
            l += 1
            for j in range(l):
                if (i != j):
                        
                    # Compute GCD
                    x = gcd(arr[i], brr[j])
    
                    # Decrement GCD value by 2
                    freq[x] -= 2
    res = []
    for i in range(len(brr)):
        if brr[i] > 0:
            res.append(brr[i])
    return res

print(solve([2, 2, 2, 2, 8, 2, 2, 2, 10]))