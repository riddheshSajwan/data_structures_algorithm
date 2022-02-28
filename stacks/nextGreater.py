'''
https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1/
'''

def nextLargerElement(A):
    #code here
    stack = []
    res = []
    for item in A[::-1]:
        while stack and item >= stack[-1]:
            stack.pop()
        if stack == []:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(item)
    return res[::-1]

print(nextLargerElement([6,8,0,1,3]))