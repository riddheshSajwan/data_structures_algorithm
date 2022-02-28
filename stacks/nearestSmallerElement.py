'''
https://www.interviewbit.com/problems/nearest-smaller-element/
'''

def prevSmaller(A):
    stack = []
    res = []
    for item in A:
        #print(stack,res)
        while stack and stack[-1] >= item:
            stack.pop()
        if stack == []:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(item)
    return res

print(prevSmaller([4, 5, 2, 10, 8]))