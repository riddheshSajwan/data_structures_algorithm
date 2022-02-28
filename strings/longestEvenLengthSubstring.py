'''
https://practice.geeksforgeeks.org/problems/longest-even-length-substring/0/
'''
testCases = int(input())
for case in range(testCases):
    digits = input()
    size = len(digits)
    sslen = size if size%2==0 else size-1
    #print(sslen)
    while sslen > 1:
        i = 0
        while i+sslen <= size:
            substring = digits[i:i+sslen]
            leftSum = 0
            rightSum = 0
            for left in range(0,sslen//2,1): rightSum = rightSum + int(substring[left])
            for right in range(sslen-1,(sslen//2)-1,-1): leftSum = leftSum + int(substring[right])
            if rightSum == leftSum:
                print(sslen)
                sslen = 1
                break
            else:
                i+=1
        sslen-=2
    if sslen == 0: print(0)